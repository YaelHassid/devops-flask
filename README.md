# Hello-devops-flask-project

## Overview:
This project leverages AWS services including Amazon S3, Auto Scaling Groups (ASG), and Load Balancers (LB) to create a scalable, reliable, and efficient architecture. The project aims to demonstrate how to build a distributed system that can handle varying loads while maintaining high availability and performance.

## Architecture:
1. **Amazon S3**: Used for storing a file.
2. **Auto Scaling Group (ASG)**: Automatically adjusts the number of EC2 instances based on the demand to ensure consistent performance.
3. **Load Balancer (LB)**: Distributes incoming traffic across multiple EC2 instances to ensure no single instance is overwhelmed.

## Prerequisites:
Before running this project, ensure you have the following:
- An AWS account with appropriate permissions.

## Setup Instructions:

### 1. Amazon S3
- Create a private S3 bucket.
- Upload an image file (PNG, JPG, or GIF) that you want to show when the app is running.
- Update your Flask application to use the new S3 bucket name and image file name.

### 2. Auto Scaling Group
- Create a launch template with this user data:<br />
  """#!/bin/bash
  sudo yum update -y
  sudo yum install git -y
  sudo yum install docker -y
  sudo service docker start
  sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  sudo git clone https://github.com/YaelHassid/devops-flask.git
  cd devops-flask/
  
  cat <<EOF > .env
  DB_USERNAME=postgres
  DB_PASSWORD=postgres123
  DB_NAME=usersdb
  DB_HOST=postgress_server
  DB_PORT=5432
  EOF
  
  sudo docker-compose up --build -d
  
  until sudo docker-compose exec postgress_server pg_isready -U postgres; do
    echo "Waiting for PostgreSQL to be ready..."
    sleep 5
  done
  
  sudo docker-compose exec postgress_server psql -U postgres -c "CREATE DATABASE usersdb;"
  sudo docker-compose exec postgress_server psql -U postgres -d usersdb -c "
  CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(250) NOT NULL
  );"
  
  sudo docker-compose exec postgress_server psql -U postgres -d usersdb -c "\dt" """
  
- Create an Auto Scaling Group with the Launch template you've created 

### 3. Load Balancer
- Create a Load Balancer
- Create a target group that listens on port 80 and target to port 5555
- Add the target group you've created a listener to the load balancer.

## Usage:
Access the application through the Load Balancer's DNS name provided by AWS.
Monitor the system using AWS CloudWatch for metrics related to EC2 instances, ASG, and LB.

## Contact:
For any questions or support, please contact cohenyaelh@gmail.com .

