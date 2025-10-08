# SentinelOps 🚀
**AI-Driven Observability & Anomaly Detection Pipeline**

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-%232496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kafka](https://img.shields.io/badge/Kafka-%23ED1C24.svg?style=flat&logo=apachekafka&logoColor=white)](https://kafka.apache.org/)

---

## 🌐 Overview
SentinelOps implements a **modern observability stack** combined with **AI-based anomaly detection** for logs and metrics.  
It provides **real-time insights** into system health, error rates, and unusual patterns using logs and metrics collected across services.

Key features:
- Real-time log streaming with **Kafka**  
- Metrics collection with **OpenTelemetry, Telegraf & VictoriaMetrics**  
- Visualization using **Grafana**  
- Log aggregation via **Loki**  
- Trend & anomaly detection using **Machine Learning models** (Prophet, Isolation Forest, One-Class SVM)  

---

## 🧩 Architecture
![Architecture](https://github.com/user-attachments/assets/36bf2e44-3030-46a0-a457-bfe35d1cd048)

---

## ⚙️ Tech Stack

| Component | Purpose |
|-----------|---------|
| **Docker Compose** | Orchestrates all services |
| **Kafka** | Real-time log streaming |
| **VictoriaMetrics** | High-performance time-series storage |
| **Grafana** | Visualization & dashboards |
| **Loki** | Log aggregation |
| **OpenTelemetry** | Unified observability |
| **Telegraf** | System metrics collection |
| **Python (ML)** | Anomaly detection pipelines |
| **Go (Kafka)** | High-performance log streaming |

---

## 🧪 Machine Learning Pipelines

### 1️⃣ Prophet (Trend Detection)
- Captures **daily & weekly patterns** in request rates  
- Detects abnormal **spikes or drops** in workload  

### 2️⃣ Isolation Forest
- Detects **multivariate anomalies** (request volume, session diversity, error rate)  
- Highlights **top contributing features** for each anomaly  

### 3️⃣ One-Class SVM
- Detects **rare or novel patterns**  
- Captures **low-frequency but critical anomalies**  

### 4️⃣ Trend Reports
- Generates **daily and hourly anomaly summaries**  
- Visualizes **spikes, root causes, and feature impacts**  

---

## 🧰 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/SentinelOps.git
cd SentinelOps
```

### 2️⃣ Start the Observability Stack
```bash
docker-compose up -d
```

### 3️⃣ Produce Synthetic Logs
```bash
# Python producer
python kafka/producer.py

# OR Go producer
go run kafka/producer.go
```

### 4️⃣ Consume Logs
```bash
# Python consumer
python kafka/consumer.py

# OR Go consumer
go run kafka/consumer.go
```

### 5️⃣ Run Anomaly Detection
```bash
cd ml_anomaly_detection

python isolation_forest.py
python one_class_svm.py
python prophet_trends.py
```

### 6️⃣ View Dashboards
- **Grafana** → [http://localhost:3000](http://localhost:3000)  
- **VictoriaMetrics** → [http://localhost:8428](http://localhost:8428)  
- **Loki Logs** → [http://localhost:3100](http://localhost:3100)  

---

## 📊 Sample Outputs

### 🧩 Isolation Forest Anomalies
- Detects unusual patterns in request volume, session diversity, and error rates  
- Highlights **top contributing metrics** per anomaly  

### 🌀 One-Class SVM Results
- Captures **rare or novel behavioral patterns**  
- Detects low-frequency but critical anomalies  

### 📈 Prophet Trend Forecast
- Forecasts daily and weekly traffic  
- Detects spikes and drops for proactive monitoring  

---

## 🛠️ Folder Structure

| Folder | Description |
|--------|-------------|
| `kafka/` | Log producers & consumers (Python & Go) |
| `ml_anomaly_detection/` | Anomaly detection scripts |
| `reports/` | Generated weekly/daily reports |
| `screenshots/` | Visualization assets for README |
| `docker-compose.yml` | Multi-container orchestration |

---

## 🧾 Requirements

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
pandas
numpy
matplotlib
scikit-learn
prophet
kafka-python
```

---

## 🌟 Future Enhancements
- ✅ Automatic anomaly alerting via Slack or Email  
- ✅ Integration with Promtail for log tailing  
- 🚀 Kubernetes-based scalable deployment  
- 🔍 Advanced root cause correlation engine  
---
## Demo Outputs

<img width="890" height="619" alt="image" src="https://github.com/user-attachments/assets/2daa4a55-25a5-476c-b2ee-d3d49f216938" />
<img width="965" height="610" alt="image" src="https://github.com/user-attachments/assets/b93fd19b-e37b-412f-9610-7c303a65825f" />
<img width="559" height="343" alt="image" src="https://github.com/user-attachments/assets/b1d8bbcb-fbb4-42f6-8095-36288989e6fa" />
<img width="562" height="380" alt="image" src="https://github.com/user-attachments/assets/54316033-7c34-4a25-86cc-b42fac5d8d6d" />
<img width="1141" height="645" alt="image" src="https://github.com/user-attachments/assets/b40338bc-6bf3-4185-a44e-8a4fe94f8d28" />
<img width="1145" height="640" alt="image" src="https://github.com/user-attachments/assets/bed0420a-9c15-4321-b454-a7c480ffeee7" />
<img width="1148" height="646" alt="image" src="https://github.com/user-attachments/assets/184f5bed-8a92-4df0-8674-fcf279b89b28" />




---

## 👨‍💻 Author
**Marpu Sai Mahesh**  
📍 India  
[LinkedIn](https://www.linkedin.com/in/marpumahesh/) | [GitHub](https://github.com/saimahesh19)  

---

⭐ If you like this project, consider giving it a star on GitHub!
