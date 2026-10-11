pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t week09-python-app:latest .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm -v "$WORKSPACE:/app" -w /app python:3.12-slim sh -c "pip install -q pytest && pytest -v"'
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker run --rm week09-python-app:latest'
            }
        }
    }
}
