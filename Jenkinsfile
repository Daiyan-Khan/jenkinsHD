pipeline {
    agent any  // Use any available agent

    environment {
        PYTHON_ENV = "venv"  // Define the Python environment
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/Daiyan-Khan/snake_game.git'  // Replace with your repo URL
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create and activate a virtual environment
                sh 'python3 -m venv $PYTHON_ENV'
                sh '. $PYTHON_ENV/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary dependencies, if any
                sh 'pip install -r pytest pylint flake8 black'  // Ensure you have a requirements.txt file
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests (add your test command here)
                sh 'python test.py'  // Example using pytest, adjust if you use a different testing framework
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
