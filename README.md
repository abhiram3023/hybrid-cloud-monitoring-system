# Hybrid Cloud Monitoring and Alerting System

This project is a practical implementation of a cloud monitoring solution that combines **Microsoft Azure Monitor** with **custom Python scripts** to achieve both infrastructure-level and operating system-level monitoring.

The goal of this project is to build a system that can continuously monitor performance, detect anomalies, and generate alerts in real time — similar to what is used in real-world DevOps and SRE environments.

---

## Overview

Most cloud platforms provide monitoring at the infrastructure level (CPU, memory, etc.), but they often lack visibility into system-level activities like login attempts or detailed resource behavior.

This project addresses that gap by creating a hybrid monitoring system:
- Azure Monitor handles cloud-level metrics
- Python scripts handle OS-level monitoring
- Cron jobs automate the entire workflow

This combination results in a more complete and flexible monitoring solution.

---

## Key Features

- Monitoring of CPU, memory, and disk usage  
- Detection of failed login attempts (basic security monitoring)  
- Real-time alert generation using Azure Monitor  
- Automated execution using cron jobs  
- Lightweight and efficient system with minimal resource usage  

---

## System Architecture

The system is built using a layered approach:

- An Azure Virtual Machine (Ubuntu) acts as the main environment  
- Azure Monitor tracks infrastructure metrics and triggers alerts  
- Python scripts monitor OS-level parameters such as logs and resource usage  
- Cron jobs ensure continuous and automatic execution  
- Alerts are sent via email when thresholds are exceeded  

---

## Tech Stack

- Cloud Platform: Microsoft Azure  
- Operating System: Ubuntu Server  
- Programming Language: Python 3  
- Libraries:
  - psutil (for system monitoring)
  - smtplib (for sending alerts)
- Tools:
  - Azure Monitor
  - Cron (Linux scheduler)

---

## How the System Works

1. Azure Monitor continuously tracks VM-level metrics  
2. Python scripts collect system-level data (CPU, memory, logs, etc.)  
3. Cron jobs execute these scripts at regular intervals  
4. The system checks for threshold violations  
5. Alerts are generated when abnormal conditions are detected  

---

## Experiments and Testing

To validate the system, several test scenarios were created:

- High CPU usage was simulated using background processes  
- Disk space was reduced by creating large files  
- Memory usage was increased under load conditions  
- Failed SSH login attempts were intentionally triggered  

The system successfully detected all these conditions and generated alerts accordingly.

---

## Results

- Accurate monitoring of system performance  
- Successful detection of security-related events (login failures)  
- Reliable alert generation through Azure Monitor  
- Fully automated monitoring without manual intervention  

The hybrid approach proved to be more effective than relying only on cloud-native monitoring tools. :contentReference[oaicite:0]{index=0}

---

## Limitations

- Requires manual setup and configuration  
- Limited visualization compared to advanced monitoring tools  
- Alerting system is basic and can be improved  

---

## Future Improvements

- Integration with dashboards (Grafana or Power BI)  
- AI-based anomaly detection  
- Centralized monitoring for multiple systems  
- Integration with communication tools like Slack or Teams  

---

## Project Structure
