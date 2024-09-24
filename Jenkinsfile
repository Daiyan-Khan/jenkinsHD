pipeline {
    agent any  // Use any available agent

    environment {
        PYTHON_ENV = "venv"  // Define the Python environment
    }

    stages {

        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment
                sh 'python -m venv $PYTHON_ENV'
                bat "$PYTHON_ENV\\Scripts\\activate.bat"  // Correct activation for Windows
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary dependencies, if any
                sh 'pip install -r requirements.txt'  // Ensure you have a requirements.txt file
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests (add your test command here)
                sh 'pytest'  // Example using pytest, adjust if you use a different testing framework
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
