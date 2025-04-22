from django.urls import path
from .views import RegisterView, LoginView, LogoutView, BookListView, BookDetailView, AddToCartView,AdminRegisterView, AdminLoginView, AdminDashboardView, AddBookView, DeleteBookView, view_cart, remove_from_cart, add_to_cart

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('cart/', view_cart, name='view_cart'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
    path('myadmin/register/', AdminRegisterView.as_view(), name='admin_register'),
    path('myadmin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('myadmin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('myadmin/book/add/', AddBookView.as_view(), name='add_book'),
    path('myadmin/book/delete/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
]
