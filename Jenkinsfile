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
                sh 'docker build -t week09-python-app:${BUILD_NUMBER} .'
            }
        }

        stage('Test Application') {
            steps {
                sh 'docker run --rm -e APP_VERSION=v1 week09-python-app:${BUILD_NUMBER} python -m pytest -v'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    if docker service inspect week09-app >/dev/null 2>&1; then
                        docker service update \
                            --image week09-python-app:${BUILD_NUMBER} \
                            --update-parallelism 1 \
                            --update-delay 10s \
                            week09-app
                    else
                        docker service create \
                            --name week09-app \
                            --replicas 2 \
                            --publish published=5001,target=5000 \
                            week09-python-app:${BUILD_NUMBER}
                    fi
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker service ps week09-app'
                sh 'docker service ls'
            }
        }
    }
}
