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

        stage ('Push da image'){
            steps {
                script{
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        dockerapp.push('latest')
                        dockerapp.push("${env.BUILD_ID}")
                }
            }
        }
            
    }
}