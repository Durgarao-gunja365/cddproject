pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker')
        IMAGE_NAME = 'durgarao365/cddproject'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Durgarao-gunja365/cddproject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin"
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    sh "docker push $IMAGE_NA"
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh "docker rmi $IMAGE_NAME || true"
        }
    }
}
