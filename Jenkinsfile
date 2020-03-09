pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
               sh 'echo "supersecretkey" > rtppythonmeetup/secret_key.txt'
               sh 'docker-compose -f docker-compose_test.yml build --build-arg UID=996 rtppythonmeetup-djang-dev'
               sh 'docker-compose -f docker-compose_test.yml up'
            }
        }
    }
}
