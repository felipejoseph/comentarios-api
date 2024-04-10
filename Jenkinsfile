pipeline {
    agent any

    stages {
        stage ('Build da imagem'){
            steps {
                script{
                    dockerapp = docker.build("felipejoseph/comentarios-api:${env.BUILD_ID}", '-f ./app/Dockerfile ./app')
                }
            }
        }
            
    }
}