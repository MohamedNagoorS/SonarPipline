pipeline{
    agent any 
    environment{
        PYTHON_PATH='C:\Users\sheik\AppData\Local\Programs\Python\Python311;C:\Users\sheik\AppData\Local\Programs\Python\Python311\Scripts'
    }
    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Build'){
            steps{
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip install requirements.txt
                '''
            }
        }
        stage('SonarAnalysis'){
            environment{
                SONAR_TOKEN=credentials('sonarqube-token')
            }
            steps{
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner.bat ^
                -Dsonar.projectKey=Jenkins-Script ^
                -Dsonar.sources=." ^
                -Dsonar.host.url=http://localhost:9000 ^
                -Dsonar.token=%SONAR_TOKEN% ^
                '''
            }
        }
    }
    post{
        success{
            echo "DONE SUCCESSFULLY"
        }
        failure{
            echo "SOMETHING IS WRONG"
        }
    }
    
}
