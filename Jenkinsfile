pipeline {

    Agent any

    stages{

        stage('Clone Code'){
            steps{
                git https://github.com/yash1015/CI-CD-Pipeline-for-NotesTaker-App.git
            }
        }

        stage('Docker Image'){
            steps{
                sh ' docker build -t notes.app .'
            }
        }

        stage('Docker Container '){
            steps{
                sh ' docker run -d -p 5000:5000 notes-app'
            }
        }
        

       
        









    }
}