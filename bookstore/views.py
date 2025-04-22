from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book, UserProfile

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'bookstore/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'bookstore/book_detail.html', {'book': book})

class AddToCartView(View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        cart[str(pk)] = cart.get(str(pk), 0) + 1
        request.session['cart'] = cart
        return redirect('book_list')

class AdminRegisterView(View):
    def get(self, request):
        return render(request, 'registration/admin_register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, is_admin=True)
        return redirect('login')

class AdminLoginView(View):
    def get(self, request):
        return render(request, 'registration/admin_login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and hasattr(user, 'userprofile') and user.userprofile.is_admin:
            login(request, user)
            return redirect('admin_dashboard')
        return render(request, 'registration/admin_login.html', {'error': 'Invalid admin credentials'})

class AdminDashboardView(View):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.userprofile.is_admin:
            return redirect('admin_login')
        books = Book.objects.all()
        return render(request, 'bookstore/admin_dashboard.html', {'books': books})

class AddBookView(View):
    def get(self, request):
        if not request.user.userprofile.is_admin:
            return redirect('admin_login')
        return render(request, 'bookstore/add_book.html')

    def post(self, request):
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
            inventory=request.POST['inventory'],
            description=request.POST['description']
        )
        return redirect('admin_dashboard')

class DeleteBookView(View):
    def post(self, request, pk):
        if request.user.userprofile.is_admin:
            book = get_object_or_404(Book, pk=pk)
            book.delete()
        return redirect('admin_dashboard')

def add_to_cart(request, book_id):
    cart = request.session.get('cart', {})
    cart[str(book_id)] = cart.get(str(book_id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    if str(book_id) in cart:
        del cart[str(book_id)]
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        item_total = book.price * quantity
        total_price += item_total
        cart_items.append({
            'book': book,
            'quantity': quantity,
            'total': item_total
        })

    return render(request, 'bookstore/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })