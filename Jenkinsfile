pipeline {
  agent any
  environment {
  	  SONARQUBE_URL     = 'http://localhost:9000'
      SONARQUBE_KEY     = credentials('sonar-key')
      REPOSITORY = 'lasanthar78/flask-cicd-bootstrap'
      DOCKER_USER_NAME = 'lasanthar78'
      DOCKER_PASSWORD = credentials('dockerpassword')
      VERSION = 'latest'  	  
  }
  
  
  stages {  	    	  
      stage('compile') {
         steps {
         sh 'python -m pip install --upgrade pip'
         sh 'if [ -d "venv" ]; then rm -Rf venv; fi && virtualenv venv && . venv/bin/activate && pip install -r requirements-dev.txt && pytest -v -o junit_family=xunit1 --cov=. --cov-report xml:coverage.xml --junitxml=nosetests.xml'             
         }
      }                     
      stage('analysis') {
      	when {
        	branch 'main'  
      	}
        steps {     
            sh 'export PATH=/home/jenkins/software/sonar-scanner/bin:$PATH && sonar-scanner -Dsonar.host.url=$SONARQUBE_URL -Dsonar.login=$SONARQUBE_KEY'                                                       
        }
      }                       
      stage('container build and push') {
      	when {
        	branch 'main'  
      	}
         steps {         	
         	sh 'docker build . -t $REPOSITORY:$VERSION'
				sh 'echo "$DOCKER_PASSWORD" | docker login --username $DOCKER_USER_NAME --password-stdin'				
				sh 'docker push $REPOSITORY:$VERSION'
         }
      }
  }  
}
