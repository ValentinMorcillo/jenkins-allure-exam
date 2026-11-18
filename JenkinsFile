pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out successfully.'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    ./.venv/bin/python -m pip install --upgrade pip
                    ./.venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh './.venv/bin/pytest test_1.py --alluredir=allure-results'
                }
            }
        }
    }

    post {
        always {
            allure 'allure-results'
        }
    }
}