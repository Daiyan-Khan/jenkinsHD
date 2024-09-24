pipeline {
    agent any  // Use any available agent

    environment {
        PYTHON_ENV = "venv"  // Define the Python environment
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Task: Checkout the source code from GitHub
                git url: 'https://github.com/myhuy612/SIT223-6.2HD-DevOps-Pipeline.git', branch: 'main'
                echo "Code has been checked out from GitHub"
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment
                bat 'python -m venv %PYTHON_ENV%'  // Use 'bat' for Windows commands
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat'  // Correct activation for Windows
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary dependencies
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && pip install -r requirements.txt'  // Ensure virtual environment is activated
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests (ensure virtual environment is activated)
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && python test.py'  // Running your test script
            }
        }

        stage('Build') {
            steps {
                // If you have a build step, add it here
                echo 'Building the application...'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy your application (add your deployment steps here)
                echo 'Deploying the application...'
            }
        }
    }

    post {
        success {
            echo 'Build and Tests passed!'
        }
        failure {
            echo 'Build or Tests failed!'
        }
        always {
            // Cleanup actions if needed
            echo 'Cleaning up...'
        }
    }
}
