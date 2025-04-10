# cddproject
 # Build and Push Docker Image to Docker Hub using Jenkins


🛠️ CI/CD Pipeline Setup This project uses Jenkins for continuous integration and Docker for containerization.

# Workflow: Jenkins Pipeline:

Configured via a Jenkinsfile stored in the root of the repository.

Automatically triggers on new commits to the main branch.

Steps Performed:

Clones the GitHub repository.

Builds a Docker image using the Dockerfile.

Installs dependencies from requirements.txt.

Pushes the Docker image to Docker Hub (if login is successful).

Cleans up the workspace after build.

Docker Integration:

Uses Python 3.9-slim base image.

Application code is copied into the container.

Required packages are installed inside the container.

✅ Build Status Jenkins will show whether the build passed or failed directly on your Jenkins dashboard.

# 🚀 CI/CD with Jenkins and Docker — Step-by-Step Commands 
🧰 Prerequisites Jenkins installed and running

Docker installed and running

GitHub repo configured with Dockerfile, requirements.txt, and Jenkinsfile

Docker Hub account (for pushing images)

🔧 Step-by-Step Commands

Clone your repository (if needed):
bash
git clone https://github.com/Durgarao-gunja365/cddproject.git cd cddproject

Start Jenkins and open the Jenkins dashboard:
bash
sudo systemctl start jenkins
Go to http://localhost:8080 or your Jenkins server IP

Create a New Jenkins Pipeline Job: Click on "New Item".

Name it (e.g., cddproject).

Select "Pipeline" and click OK.

Scroll down to Pipeline script from SCM.

Select Git and enter your repository URL: https://github.com/Durgarao-gunja365/cddproject.git

Click Save.

Run the Pipeline Job: Click "Build Now"
Jenkins will:

Clone the repo

Build Docker image using Dockerfile

Install dependencies

(Optionally) push image to Docker Hub

Docker Commands (manually if needed): 📦 Build the Docker Image: bash docker build -t durgarao365/cddproject . 🔍 Check Docker Images: bash docker images ▶️ Run the Docker Container: bash docker run -p 5000:5000 durgarao365/cddproject You can now access the app at http://localhost:5000

Login to Docker Hub (for pushing): bash docker login

Push Docker Image to Docker Hub: bash docker tag durgarao365/cddproject durgarao365/cddproject:latest docker push durgarao365/cddproject:latest
