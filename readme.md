###### &#x20;TaskFlow - DevOps Enabled To-Do Application



\## Overview



TaskFlow is a containerized To-Do web application built using Flask and MySQL. This project demonstrates modern DevOps practices including containerization, CI/CD automation, monitoring, security scanning, and observability.



\---



\## Application Interface



TaskFlow allows users to:



\* Add Tasks

\* Mark Tasks as Completed

\* Delete Tasks

\* Store Data Persistently in MySQL







\## Containerization with Docker



The entire application is containerized using Docker and managed using Docker Compose.



\### Services Deployed



\* Flask Application

\* MySQL Database

\* Nginx Reverse Proxy

\* Prometheus

\* Grafana



\### Docker Architecture



```text

User

&#x20;│

&#x20;▼

Nginx

&#x20;│

&#x20;▼

Flask App

&#x20;│

&#x20;▼

MySQL

```



\---



\##  CI/CD Pipeline



The project uses GitHub Actions for Continuous Integration and Continuous Delivery.



Whenever code is pushed to GitHub:



1\. GitHub Actions is triggered

2\. Docker image is built automatically

3\. Docker Hub authentication occurs

4\. Updated image is pushed to Docker Hub



\### CI/CD Workflow



!\[GitHub Actions](images/github-actions.png)



\### Pipeline Flow



```text

Developer

&#x20;  │

&#x20;  ▼

Git Push

&#x20;  │

&#x20;  ▼

GitHub Actions

&#x20;  │

&#x20;  ▼

Docker Build

&#x20;  │

&#x20;  ▼

Docker Hub Push

```



\---



\##  Security Enhancements



Security measures implemented:



\* Environment Variables

\* Docker Isolation

\* Health Checks

\* Trivy Vulnerability Scanning



\##  Monitoring \& Observability



Prometheus collects metrics from the application and Grafana visualizes them through dashboards.



Monitoring helps identify:



\* Application Health

\* Service Availability

\* System Performance

\* Infrastructure Metrics





\---



\##  Technology Stack



| Category         | Technology     |

| ---------------- | -------------- |

| Backend          | Flask          |

| Database         | MySQL          |

| Reverse Proxy    | Nginx          |

| Containerization | Docker         |

| Orchestration    | Docker Compose |

| CI/CD            | GitHub Actions |

| Registry         | Docker Hub     |

| Monitoring       | Prometheus     |

| Visualization    | Grafana        |

| Security         | Trivy          |



\---



\##  Project Structure



```text

todoapp/

│

├── .github/

│   └── workflows/

│       └── ci-cd.yml

│

├── mysql/

├── nginx/

├── static/

├── templates/

│

├── app.py

├── Dockerfile

├── docker-compose.yml

├── prometheus.yml

├── .gitignore

└── README.md

```



\---



\##  Running the Project



Clone the repository:



```bash

git clone <repository-url>

cd todoapp

```



Start all services:



```bash

docker compose up --build -d

```



Verify running containers:



```bash

docker compose ps

```



Stop services:



```bash

docker compose down

```



\---



\##  Learning Outcomes



Through this project, I gained hands-on experience with:



\* Flask Development

\* MySQL Integration

\* Docker \& Docker Compose

\* Nginx Reverse Proxy

\* GitHub Actions CI/CD

\* Docker Hub Integration

\* Trivy Security Scanning

\* Prometheus Monitoring

\* Grafana Dashboard Creation

\* DevOps Best Practices



\---



\##  Author



\*\*Balasoorya\*\*



DevOps | Docker | CI/CD | Monitoring | Cloud Computing



