pipeline{
    agent any 
    environment{
        PYTHON_PATH = "C:\\Users\\sheik\\AppData\\Local\\Programs\\Python\\Python311;C:\\Users\\sheik\\AppData\\Local\\Programs\\Python\\Python311\\Scripts"
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
                pip install -r requirements.txt
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
                -Dsonar.token=sqp_2f6928eacb6fa646c185441562a343b5f964c754 ^
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
