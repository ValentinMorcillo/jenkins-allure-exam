pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_FILTER',
            choices: ['test_1.py', 'test_2.py'],
            description: 'Select the test file to execute'
        )
    }

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
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh '''
                        rm -rf allure-results
                        ./.venv/bin/pytest "${params.TEST_FILTER}" --alluredir=allure-results
                    '''
                }
            }
        }
    }

    post {
        always {
            allure commandline: 'Allure_Mac', includeProperties: false, jdk: '', resultPolicy: 'LEAVE_AS_IS', results: [[path: 'allure-results']]
        }
    }
}