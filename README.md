## setting up git on the ec2 machine:
  - sudo yum update -y
  - sudo yum install git -y
  - git — version
## setting up docker on the ec2 machine:
  - sudo yum update -y
  - sudo yum install docker -y
  - sudo systemctl start docker
  - sudo systemctl enable docker
  - sudo usermod -a -G docker $(whoami)
  - newgrp docker
## setting up docker-compose on the ec2 machine:
  - sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
  - sudo chmod +x /usr/local/bin/docker-compose
  - docker-compose version
## clone the project on the ec2 machine:
  - git clone https://github.com/YaelHassid/devops-flask.git
  - cd devops-flask
## creating a .env file:
  - nano .env
  - DB_USERNAME = postgres
    DB_PASSWORD = postgres123
    DB_NAME = 'usersdb'
    DB_HOST = 'flask-devops-yael-postgress_server-1'
    DB_PORT = 5432 
## docker-compose the project:
  - docker-compose up
