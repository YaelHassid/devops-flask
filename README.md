## setting up git on the ec2 machine:
  - sudo yum update -y
## setting up docker on the ec2 machine:
  - sudo yum update -y
  - sudo yum install docker -y
  - sudo systemctl start docker
  - sudo systemctl enable docker
  - sudo usermod -a -G docker $(whoami)
  - newgrp docker
