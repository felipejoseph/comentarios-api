pipeline {
    agent any

    stages {
        stage ('Build da imagem'){
            steps {
                script{
                    dockerapp = dockerbuild.Build("felipejoseph/comentarios-api:${env.BUILD_ID}", '-f ./app/Dockerfile ./app')
                }
            }
        }
            
    }
}