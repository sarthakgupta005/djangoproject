pipeline {
  agent {
    docker {
      image 'python:3.5.1'
    }

  }
  stages {
    stage('build') {
      parallel {
        stage('build') {
          steps {
            sh 'python --version'
          }
        }

        stage('test') {
          steps {
            echo 'test over'
          }
        }

      }
    }

    stage('final') {
      steps {
        echo 'final branch'
      }
    }

  }
}