pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/yash1015/CI-CD-Pipeline-for-NotesTaker-App.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t yashkangude87/notes-app:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh 'docker login -u yashkangude87 -p Kangude@7621'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push yashkangude87/notes-app:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}