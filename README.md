# Secure CI/CD Pipeline on Azure with DevSecOps Practices

This project demonstrates a fully automated DevSecOps pipeline for a simple Python web application. The goal is to showcase the integration of Continuous Integration, Continuous Delivery, and security practices using free and open-source tools on Azure's free-tier services.

## Project Architecture

The pipeline is built using **Azure DevOps** and is triggered automatically on every code change pushed to the main branch. The core steps of the pipeline are:

1.  **Build and Security Scans:**
    * The application is containerized using a `Dockerfile`.
    * **Static Application Security Testing (SAST):** Code is scanned with **SonarCloud** to identify vulnerabilities, bugs, and code smells.
    * **Software Composition Analysis (SCA):** The application's dependencies are checked for known vulnerabilities using **OWASP Dependency-Check**.

2.  **Deployment:**
    * The validated and scanned application is automatically deployed to an **Azure App Service** instance running on the **F1 (Free) tier**.

## Key Technologies

* **Azure DevOps:** For the CI/CD pipeline, build agents, and project management.
* **GitHub:** For source code management.
* **Python Flask:** The simple web framework used for the application.
* **Docker:** To containerize the application, ensuring consistency across environments.
* **SonarCloud:** An industry-standard tool for static code analysis.
* **OWASP Dependency-Check:** An open-source tool for finding known vulnerabilities in dependencies.
* **Azure App Service:** A cost-effective Platform as a Service (PaaS) for hosting the application.

This project highlights a "shift-left" security approach, where security is integrated early in the development lifecycle rather than as an afterthought.# my-azuredevops-project
