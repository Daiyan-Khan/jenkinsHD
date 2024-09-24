pipeline {
    agent any  // Use any available agent

    environment {
        PYTHON_ENV = "venv"  // Define the Python environment
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Task: Checkout the source code from GitHub
                git url: 'https://github.com/Daiyan-Khan/jenkinsHD.git', branch: 'main'
                echo "Code has been checked out from GitHub"
                
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create a virtual environment
                bat 'python -m venv %PYTHON_ENV%'  // Use 'bat' for Windows commands
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat'  // Correct activation for Windows
                sh 'venv/Scripts/activate && pip install pytest pylint flake8 black'
            }
        }

        stage('Run Code Quality Checks') {
            steps {
                script {
                    // Activate the virtual environment and run Pylint
                    sh 'venv/Scripts/activate && pylint snakegame.py'
                    
                    // Run Flake8
                    sh 'venv/Scripts/activate && flake8 snakegame.py'
                    
                    // Format code using Black
                    sh 'venv/Scripts/activate && black snakegame.py'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests (add your test command here)
                bat 'call %PYTHON_ENV%\\Scripts\\activate.bat && python test.py'  // Example using pytest
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
