# 🔌 Smart Meter Data Dashboard

This project simulates, validates, and visualizes smart electricity meter data—mimicking real-world data operations in utility and energy analytics. It includes a custom-built Streamlit dashboard for monitoring usage patterns, detecting anomalies, and demonstrating key skills in data cleaning, analysis, and real-time reporting.

---

## 🚀 Live Demo

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-success?style=flat&logo=streamlit&logoColor=white&labelColor=ff4b4b)](https://smart-meter-dashboard-4wjhgvtkgukztsntg752bj.streamlit.app/)

Explore the live dashboard here:  
**https://smart-meter-dashboard-4wjhgvtkgukztsntg752bj.streamlit.app/**

---

## 📈 Features

- Simulates hourly energy usage data from 100+ meters over 7 days
- Injects realistic anomalies (missing data, duplicates, outliers)
- Performs automated data validation and anomaly detection
- Visualizes data through:
  - Line graphs (per-meter usage)
  - Heatmaps (hourly average usage across meters)
- Fully interactive dashboard built with Streamlit

---

## 🛠 Technologies Used

- Python
- Pandas, NumPy, Matplotlib, Seaborn, SciPy
- Streamlit for dashboard UI

---

## 📁 Project Structure

```bash
smart-meter-dashboard/
├── simulate_data.py         # Script to generate synthetic meter data
├── validate_data.py         # Data validation and anomaly detection
├── dashboard.py             # Streamlit dashboard app
├── smart_meter_data.csv     # Sample generated dataset
├── requirements.txt         # Project dependencies
└── README.md
```

---

## 🔧 How to Run Locally

 **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/smart-meter-dashboard.git
   cd smart-meter-dashboard

  pip install -r requirements.txt

  streamlit run dashboard.py
```
