# 🛡️ Malwatch – malware watch platform

CyberSentinel – AI-Powered Network Security Scanning & Protection System
مال ووتش – منصّة لرصد وتتبع البرمجيات الضارة"


"Threat Intelligence Platform"

---

## 📚 Table of Contents
- [👥 Contributors](#-contributors)
- [📖 Project Overview](#-project-overview)
- [🎯 Project Goals](#-project-goals)
- [🛠️ System Architecture](#️-system-architecture)
- [⚙️ How It Works](#️-how-it-works)
- [🧠 AI & Machine Learning](#-ai--machine-learning)
- [📱 Frontend Implementation](#-frontend-implementation)
- [📦 Backend Architecture](#-backend-architecture)
- [🧰 Technologies Used](#-technologies-used)
- [🌟 Key Features](#-key-features)
- [🙌 Acknowledgments](#-acknowledgments)
- [🔮 Future Work](#-future-work)

---

## 👥 Contributors

This project was developed by the **CyberSentinel Team**, Computer Science Department, Mansoura University.

#### Team Members
* [Ibrahim Hegazi](https://www.linkedin.com/in/ibrahim-hegazi/) **[Team Leader & AI Engineer]**  
* [Other team members with roles can be listed here]

---

## 📖 Project Overview

CyberSentinel is a smart network scanning and vulnerability assessment tool combining traditional pentesting methods with AI-based analysis. It supports Windows, Linux live USB boot, and Android platforms, enabling users to identify security weaknesses in their home or office networks quickly and effectively.

---

## 🎯 Project Goals

- Provide automated discovery of devices and services on local networks  
- Detect open ports and insecure protocols  
- Identify known vulnerabilities using CVE databases and Shodan API  
- Use AI/ML to classify risks and generate actionable remediation guidance  
- Deliver clear, user-friendly reports in HTML and PDF formats  
- Ensure cross-platform compatibility for broad accessibility

---

## 🛠️ System Architecture

CyberSentinel consists of these main components:

- **Network Scanner:** Uses Python libraries (Scapy, Nmap) for active scanning and reconnaissance  
- **Vulnerability Engine:** Integrates Shodan API and CVE Search for risk identification  
- **AI Layer:** ML and NLP models for risk classification and human-readable recommendations  
- **Frontend UI:** Flutter (mobile), React + Electron (desktop) for cross-platform interface  
- **Database:** SQLite for local storage, Firebase for cloud synchronization  
- **Reporting:** Generates interactive HTML and PDF vulnerability reports  

---

## ⚙️ How It Works

1. User initiates a network scan via the UI  
2. Scanner detects all connected devices, open ports, and running services  
3. Vulnerability engine cross-references findings with CVE databases and Shodan  
4. AI module classifies risks and generates natural language explanations  
5. Results and reports are displayed in the UI and optionally saved/exported  
6. User reviews recommendations and takes remediation actions

---

## 🧠 AI & Machine Learning

- **Classification:** Assigns severity levels (Critical, High, Medium, Low) to detected vulnerabilities  
- **Clustering:** Groups similar devices or vulnerabilities for pattern recognition  
- **NLP:** Converts technical scan data into understandable reports and remediation steps  
- **Model Training:** Utilizes Python ML libraries (scikit-learn) and GPT API for enhanced text generation  
- **Explainability:** Offers transparent reasoning behind AI risk assessments

---

## 📱 Frontend Implementation

- Developed with **Flutter** for mobile (Android)  
- **React + Electron** for desktop versions (Windows/Linux)  
- Features include dashboard views, scan initiation, progress tracking, and report viewing  
- Responsive and accessible UI design for ease of use

---

## 📦 Backend Architecture

- Python-based scanning and AI services  
- RESTful APIs supporting frontend communication  
- Local database using SQLite; cloud sync via Firebase  
- Scalable and modular codebase designed for easy maintenance and expansion

---

## 🧰 Technologies Used

- **Programming Languages:** Python, Dart (Flutter), JavaScript (React, Electron)  
- **Scanning Tools:** Scapy, Nmap  
- **APIs:** Shodan API, CVE Search  
- **AI/ML:** scikit-learn, GPT API, custom NLP models  
- **Databases:** SQLite, Firebase  
- **Reporting:** HTML, PDF (ReportLab)  
- **Platforms:** Windows, Linux (bootable), Android

---

## 🌟 Key Features

- Automated device and service discovery on local networks  
- Open ports and protocol identification  
- Real-time CVE vulnerability matching  
- AI-powered risk classification and recommendations  
- Cross-platform compatibility (desktop, boot media, mobile)  
- Exportable HTML and PDF detailed reports  
- User-friendly interface with charts and tables  
- Offline scanning and AI analysis capability  

---

## 🙌 Acknowledgments

Special thanks to our faculty advisors and external consultants for their invaluable guidance and support throughout this project.

---

## 🔮 Future Work

- Integration with IoT device security scanning  
- Real-time threat alerts and notifications  
- Enhanced historical scan comparisons and trend analysis  
- Subscription service for continuous CVE database updates  
- Web-based dashboard for remote monitoring  
- Incorporate advanced AI models for zero-day vulnerability detection  

---


