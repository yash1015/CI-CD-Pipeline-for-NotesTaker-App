pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/yash1015/CI-CD-Pipeline-for-NotesTaker-App.git'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f notes-container || true'
            }
        }

        stage('Remove Old Image') {
            steps {
                sh 'docker rmi -f notes-app || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t notes-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name notes-container notes-app'
            }
        }
    }
}