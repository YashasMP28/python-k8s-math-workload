🧮 Python Kubernetes Math Evaluator (Workload)
📌 Project Overview
This project implements a containerized Python application that evaluates mathematical expressions.
The application is deployed as a Kubernetes Job on Minikube, following the Twelve-Factor App principles.

🚀 Features
Evaluate user-provided mathematical expressions securely.
Containerized with Docker for portability.
Deployable as a Job in Kubernetes using Minikube.
Clean project structure with Python virtual environment.


📂 Project Structure
bash
Copy code
k8s-math-workload/
│── app/
│   └── main.py         # Python math evaluator logic
│── Dockerfile          # Docker image definition
│── job.yaml            # Kubernetes Job manifest
│── requirements.txt    # Python dependencies
└── README.md           # Project documentation


🛠️ Technologies Used

Python 3.10
Docker
Kubernetes (Minikube)
kubectl CLI
Git + GitHub
VS Code


⚡ Setup Instructions

1️⃣ Build the Docker Image
bash
Copy code
docker build -t math-evaluator:1.0 .
2️⃣ Load Image into Minikube
bash
Copy code
minikube image load math-evaluator:1.0
3️⃣ Apply Kubernetes Job
bash
Copy code
kubectl apply -f job.yaml
4️⃣ Check Pods
bash
Copy code
kubectl get pods
5️⃣ View Logs (Job Output)
bash
Copy code
kubectl logs <pod-name>


📖 Example Output

makefile
Copy code
Evaluating: 10*(5+2)-3
Result: 67


📌 Project Requirements Reference

Develop a workload in Python for math expression evaluation.
Deploy workload as a Job in Minikube using Docker containers.
Separate client project to invoke workload.
Follow Twelve-Factor App principles.
Use Python virtual environment, GitHub, and VS Code.


👨‍💻 Author

Yashas M.P
