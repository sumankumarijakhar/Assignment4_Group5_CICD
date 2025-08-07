
# Assignment 4 - CI/CD on Kubernetes (Group 5)

## Course
**INFO8995 - Container and Orchestration (Spring 2025 - Section 1)**

## Group Members
- Keerthana Garimella
- Preethi Jakhar
- Suman Kumari Jakhar

## Objective
This project demonstrates how to deploy Jenkins on Kubernetes using Ansible and Helm. A simple CI/CD pipeline is created to simulate software delivery, using GitHub as the source. The pipeline includes cloning the repo, a dummy build step, and a test step that echoes a success message.

## Technologies Used
- Kubernetes (Docker Desktop)
- Ansible
- Helm
- Jenkins
- GitHub
- WSL (Ubuntu)

## Instructions

### 1. Deploy Jenkins to Kubernetes
```bash
ansible-playbook up.yaml
```
Wait ~2–3 mins. Then open [http://localhost:32000](http://localhost:32000)  
Login: `admin` / `admin123`

### 2. Create Jenkins Pipeline
- Go to **New Item → Pipeline**
- Name: `Group5-Assignment4`
- Scroll to **Pipeline** section
- Paste the contents from `jenkins-demo-app/Jenkinsfile`
- Save and run

### 3. Pipeline Overview
The pipeline includes:
- ✅ Clone stage (GitHub repo)
- ✅ Build stage (prints "Building...")
- ✅ Test stage (prints "✅ All tests passed!")

### 4. Teardown Jenkins
```bash
ansible-playbook down.yaml
```
