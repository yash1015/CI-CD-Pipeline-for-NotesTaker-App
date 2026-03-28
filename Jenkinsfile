pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main' , url: 'https://github.com/yash1015/CI-CD-Pipeline-for-NotesTaker-App.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t yashkangude87/notes-app:latest .'
            }
        }

        stage('Login to Docker Hub for build') {
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
            sh '''
            export KUBECONFIG=/var/lib/jenkins/kubeconfig
            kubectl apply -f k8s/deployment.yaml --validate=false
            kubectl apply -f k8s/service.yaml
            '''
    }
}
    }
}