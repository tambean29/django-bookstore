pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                dir('D:/Bookstore2/bookstore_project') {
                    script {
                        docker.build("django-bookstore")
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('D:/Bookstore2/bookstore_project') {
                    script {
                        bat 'docker run --rm django-bookstore python manage.py test'
                    }
                }
            }
        }

        stage('Deploy') 
        {
            steps {
                dir('D:/Bookstore2/bookstore_project') {
                    script {
                        bat 'docker-compose up -d'
                    }
                }
            }
        }
    }
}
