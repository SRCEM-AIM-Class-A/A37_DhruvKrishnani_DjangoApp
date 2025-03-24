Assignment 2: Build a Multi-App Django Project and Deploy with Docker
Objective: Create a Django application with the following requirements: • The project must have multiple apps.
• No database should be used.
• Include a Dockerfile to containerize the application.
• Write a Jenkinsfile to automate the build pipeline.
• Push the Docker image to Docker Hub.

Project Overview -
Django_App is a Django web application containing multiple apps (core, dashboard, reports) with static views. The project is containerized using Docker and supports automated deployment with Jenkins.

Features - 
Multi-app Django project (Core, Dashboard, Reports)
Static pages with Bootstrap-based UI
No database required (Only templates & views)
Containerized with Docker
CI/CD integration with Jenkins
Docker image hosted on Docker Hub
🛠 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/SRCEM-AIM-Class-A/A64_viraj_yawale.git
cd Assignment2
2️⃣ Run with Django (Without Docker)
pip install -r requirements.txt
python manage.py runserver
➡️ Open http://127.0.0.1:8000/ in your browser.

🐳 Run with Docker
1️⃣ Build the Docker Image
docker build -t studentproject .
2️⃣ Run the Container
docker run -p 8000:8000 studentproject
➡️ Open http://127.0.0.1:8000/ in your browser.

📌 CI/CD Pipeline (Jenkins)
1️⃣ Create a Jenkinsfile
This project includes a Jenkinsfile that:

Pulls code from GitHub

Builds a Docker image

Pushes the image to Docker Hub

2️⃣ Push Docker Image to Docker Hub
docker tag studentproject your-dockerhub-username/studentproject:v1
docker push your-dockerhub-username/studentproject:v1
➡️ Now anyone can pull it using:

docker pull your-dockerhub-username/studentproject:v1
Links
GitHub Repository: https://github.com/SRCEM-AIM-Class-A/A37_DhruvKrishnani_DjangoApp

Docker Hub Image: https://hub.docker.com/repository/docker/dhruvkrishnani2/studentproject/general
