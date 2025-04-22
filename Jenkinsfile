pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('django-bookstore')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image('django-bookstore').inside {
                        sh 'python manage.py test'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.image('django-bookstore').run('-p 8000:8000')
                }
            }
        }
    }
}
