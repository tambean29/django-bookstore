Project Overview: 
A bookstore django web-application with user and admin login and registration, the admin can add and delete books and manage inventory. The user can view the available books and also add them to cart, view the cart and remove from cart.

Setup and Run instructions: 
    Requirement: 
    [!reuirements file](./requirements.txt)
    docker desktop
    Jenkins UI
    MySQL8.0
    MySQL Workbench

    Steps:
    1. Clone the reository
    git clone https://github.com/tambean29/django-bookstore
    2. create virtual environment and activate
    python -m venv myvenv
    ./myvenv/Scripts/activate.bat (for windows)
    3. Install Dependencies
    pip install -r requirements.txt
    4. Run locally
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

    Tech Stack Used:
    Backend: Django 5.2, python 3.12.1
    Database: MySQL 8.0 (MySQL Workbench)
    Frontend: HTML
    CI/CD: Jenkins
    Containerization: Docker

Demo Video of Project:
![demo-gif](./assets/django-bookstore-demo.gif)

Docker Usage Notes:
1. Build and run with docker:
docker-compose up --build

2. Then access the app at http://localhost:8000.


Jenkins Usage notes:
 It is used to automate build, test and deploy of the bookstore project.
 1. it builds docker image.
 2. Runs unit tests if available.
 3. Deployes the container.

 To run:
 1. Open Jenkins UI. 
 2. Create a new pipeline job.
 3. In script, paste contents from Jenkinsfile.
 4. Save and build the job.
