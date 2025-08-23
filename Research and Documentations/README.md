# 🛡️ Malwatch – AI-Powered Network Security Scanning & Protection System

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Neo4j](https://img.shields.io/badge/GraphDB-Neo4j-orange)](https://neo4j.com/)  
[![Docker](https://img.shields.io/badge/Container-Docker-blue)](https://www.docker.com/)  
[![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-green)](https://github.com/features/actions)  

# What is Malwatch?

**Malwatch** is a **Cyber Threat Intelligence Knowledge Graph** that acts as a central brain for cybersecurity data. Unlike traditional threat dashboards or standalone TIPs, CTI-KG **connects vulnerabilities, adversaries, exploits, and detection rules into a unified graph**, and enhances it with **AI-driven analytics and automation**.

With malwatch, security teams can:

1. 🔗 **Aggregate and normalize threat data** from CVEs, IOCs, ATT&CK, dark web feeds, and exploits 
2. 🎯 **Correlate campaigns, TTPs, and adversary behaviors** across multiple sources
3. 🛡️ **Simulate attack paths** and visualize risk across the organization 
4. 🤖 **Automate alerts, SOAR playbooks, and remediation tickets** based on contextual intelligence 
5. 💬 **Query the graph naturally** using an NLP chatbot 
6. 🔒 **Share intelligence securely** via STIX/TAXII with trusted partners 
7. 📈 **Monitor, retrain, and improve** the system continuously based on user feedback and drift detection 

Think of Malwatch as a **virtual cybersecurity analyst** with a memory, reasoning skills, and automation capabilities: it can see the network, understand threats, and take action—providing **contextual insights and actionable recommendations** faster than manual processes.


## 📌 Table of Contents

1. [🚀 Project Overview](#-project-overview): A brief introduction to the Malwatch project, its purpose, and the problems it solves.

2. [🗂 Stakeholder & Audience Categorization](#-stakeholder--audience-categorization)

3. [🎯 Predicted Target Audience & Stakeholders](#-predicted-target-audience--stakeholders)

4. [✨ Key Features](#-key-features): Highlights the main functionalities, including threat data ingestion, knowledge graph construction, analytics, and automation.

5. [🏗 Architecture](#-architecture): Detailed diagram and explanation of the system components, data flow, and integrations.

6. [💻 Installation](#-installation): Step-by-step instructions to set up the environment, dependencies, and software prerequisites.

7. [🔧 Configuration](#-configuration): How to configure API keys, credentials, pipeline settings, and environment variables.

8. [🧠 Malwatch Pipeline Phases](#-malwatch-pipeline-phases): Overview of all phases from threat data acquisition to monitoring, including inputs, processing steps, and outputs.

9. [📊 Data Pipeline](#-data-pipeline): Details of data ingestion, normalization, enrichment, and storage for structured and unstructured sources.

10. [🤖 NLP Chatbot](#-nlp-chatbot): Description of the natural language interface for analysts to query the CTI-KG and receive contextual responses.

11. [📈 Visualization & Dashboards](#-visualization--dashboards): Details of interactive dashboards, graphs, and attack path visualizations for analysts and executives.

12. [🔌 API Endpoints](#-api-endpoints): List and description of available REST/GraphQL endpoints to access the KG, alerts, and dashboards programmatically.

13. [🔗 Integrations](#-integrations): Information on connecting with SIEMs, SOARs, TIPs, and third-party threat intelligence feeds.

14. [💡 Usage Examples](#-usage-examples): Sample queries, scripts, and workflows to demonstrate practical applications of CTI-KG.

15. [📊 Monitoring, Feedback & Logging](#-monitoring-feedback--logging): How the system tracks pipeline performance, captures analyst feedback, and maintains audit logs.

16. [🔒 Security & Compliance](#-security--compliance): Guidelines for safe data handling, access control, and adherence to GDPR, CCPA, ISO27001, and other standards.

17. [🤝 Contributing](#-contributing): Instructions for external developers to contribute, report issues, or suggest improvements.

18. [📜 License](#-license): Legal terms under which the project is released and used.

19. [🎉 Acknowledgments](#-acknowledgments): Credits to individuals, organizations, and open-source projects that contributed.

20. [📚 References / Resources](#-references--resources): List of documents, standards, libraries, and external links used throughout the project.


## 🚀 Project Overview

The **Malwatch** is designed to consolidate, analyze, and operationalize threat intelligence into a **centralized platform**.  

### Motivation
Organizations face **overwhelming volumes of threat data** from structured sources (CVEs, ATT&CK, CAPEC, vulnerability scans) and unstructured sources (blogs, APT notes, leak sites). Security teams often struggle to correlate data, prioritize risks, and proactively mitigate attacks. CTI-KG addresses these challenges with **AI-enhanced intelligence and automation**, enabling faster, context-aware decisions.

### High-Level Goals
1. Integrate **structured and unstructured threat intelligence** into a unified database.  
2. Enable **context-aware risk scoring** and prioritization of vulnerabilities.  
3. Apply **AI-driven analytics** for anomaly detection, predictive scoring, and attack simulations.  
4. Provide **automation & orchestration** with SOAR-ready playbooks and alerting.  
5. Deliver **interactive visualization & dashboards** for decision support.  
6. Facilitate **collaboration and secure threat sharing** via STIX/TAXII and TIP integrations.

---

## 🗂 Stakeholder & Audience Categorization

This table clarifies the distinctions between different groups interacting with Malwatch, their roles, and the rationale for separating them.  

| Category                                 | Description                                                                     | Examples                                                                                       | Why Distinguish?                                                                                                                      |
| ---------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Target Audience**                      | End users of the system who benefit directly from the outputs                   | SOC Analysts, CTI Teams, Executives, Blue Teams                                                | They consume intelligence, dashboards, alerts, and reports. Focus on usability and workflow impact.                                   |
| **Stakeholders**                         | Groups or individuals who influence, govern, or are impacted by the project     | CISO, Risk Officers, Legal Counsel, Regulators, Business Unit Leaders                          | They set priorities, compliance, policies, or funding. Focus on governance, strategy, and high-level reporting.                       |
| **Developers / Contributors**            | Technical team responsible for building, maintaining, or integrating the system | Data Engineers, ML/AI Engineers, Security Automation Engineers, Application Security Engineers | They are involved in creating pipelines, analytics, automation, and visualization. Focus on design, integration, and maintainability. |
| **External / Third-Party Collaborators** | Organizations or partners that integrate or exchange data with the system       | MSSPs, TIPs, CERTs/CSIRTs, Research Institutes                                                 | They provide or consume threat intelligence, shared insights, or collaborate on research and incident response.                       |

---

## 🎯 Predicted Target Audience & Stakeholders

## 1. Target Audience

| Stakeholder Group | Roles / Examples | Main Interactions & Benefits | Relevant CTI-KG Phases |
|------------------|-----------------|-----------------------------|-----------------------|
| Security Operations & SOC Teams | SOC Analysts (Level 1–3) | Monitor alerts, triage incidents, investigate anomalies | Phase 6, Phase 9 |
|  | Incident Response (IR) Teams | Conduct forensic analysis and remediation planning | Phase 6, Phase 7, Phase 8 |
|  | Threat Hunters | Proactively search for malicious activity within the network | Phase 6, Phase 7 |
|  | Malware Analysts | Analyze malware behavior and map it to TTPs | Phase 4, Phase 5, Phase 6 |
|  | Blue Team Members | Defend network infrastructure and endpoints | Phase 6, Phase 8 |
| Cyber Threat Intelligence (CTI) Teams | CTI Analysts | Collect, normalize, and enrich threat data from multiple sources | Phase 1, Phase 2 |
|  | CTI Researchers | Correlate campaigns, TTPs, and adversary groups | Phase 5, Phase 6 |
|  | Threat Intel Leads / Managers | Set intelligence priorities and integration strategies | Phase 2, Phase 5, Phase 12 |
|  | Open-Source Intelligence (OSINT) Researchers | Monitor dark web, leak sites, and underground forums | Phase 1, Phase 2 |

---

## 2. Stakeholders

| Stakeholder Group | Roles / Examples | Main Interactions & Benefits | Relevant CTI-KG Phases |
|------------------|-----------------|-----------------------------|-----------------------|
| Red & Purple Teams | Penetration Testers | Simulate attacks and validate defense postures | Phase 7 |
|  | Adversary Simulation Specialists | Model attack paths based on KG insights | Phase 6, Phase 7 |
|  | Purple Team Coordinators | Coordinate between Red and Blue teams using intelligence-driven simulations | Phase 7, Phase 9 |
| IT & Security Infrastructure Teams | Network Security Engineers | Manage firewalls, VPNs, IDS/IPS, and WAFs | Phase 6, Phase 8 |
|  | Cloud Security Teams | Monitor AWS, Azure, GCP workloads, and SaaS apps | Phase 6, Phase 8 |
|  | Endpoint & Device Security Teams | Deploy and manage EDR, antivirus, and patch management | Phase 6, Phase 8 |
|  | DevSecOps Teams | Integrate threat intelligence into CI/CD pipelines and automated testing | Phase 2, Phase 8 |
| Risk Management & Governance | Chief Information Security Officer (CISO) | Oversee security strategy, risk posture, and KPIs | Phase 6, Phase 12 |
|  | Risk & Compliance Officers | Ensure compliance with GDPR, CCPA, ISO27001, and other regulations | Phase 6, Phase 12 |
|  | IT Audit Teams | Evaluate security processes, policies, and incident response effectiveness | Phase 6, Phase 12 |
|  | Business Continuity / Disaster Recovery Planners | Assess threat impact on critical operations | Phase 6, Phase 12 |
| Executives & Decision Makers | CTOs / CIOs | Strategic decision-making for IT and security architecture | Phase 9, Phase 12 |
|  | Board Members / Executive Leadership | High-level risk overview, investment justification | Phase 9, Phase 12 |
|  | Business Unit Leaders | Understand security impact on critical assets and operations | Phase 6, Phase 9 |

---

## 3. Developers / Contributors

| Stakeholder Group | Roles / Examples | Main Interactions & Benefits | Relevant CTI-KG Phases |
|------------------|-----------------|-----------------------------|-----------------------|
| Software & Security Developers | Application Security Engineers | Integrate KG insights into secure development workflows | Phase 3, Phase 8 |
|  | Security Automation Engineers | Implement SOAR playbooks and automated remediation | Phase 8, Phase 9 |
|  | Data Engineers | Manage ingestion pipelines, normalization, and enrichment of threat data | Phase 1, Phase 2 |
|  | ML/AI Engineers | Develop anomaly detection, predictive scoring, and analytics models | Phase 4, Phase 6 |

---

## 4. External / Third-Party Collaborators

| Stakeholder Group | Roles / Examples | Main Interactions & Benefits | Relevant CTI-KG Phases |
|------------------|-----------------|-----------------------------|-----------------------|
| Third-Party & Community Stakeholders | Managed Security Service Providers (MSSPs) | Monitor client environments using KG insights | Phase 6, Phase 9 |
|  | Threat Intelligence Providers / TIPs | Integrate external intelligence and share structured data | Phase 1, Phase 2 |
|  | CERTs / CSIRTs (National or Sectoral) | Collaborate on incidents and campaigns | Phase 5, Phase 6 |
|  | Research Institutions & Universities | Leverage KG for academic research and security studies | Phase 3, Phase 5 |
|  | Partners & Vendors | Receive curated threat intelligence feeds for joint security operations | Phase 6, Phase 9 |
| Regulatory & Legal Stakeholders | Legal Counsel | Assess compliance, liability, and data privacy implications | Phase 6, Phase 12 |
|  | Privacy Officers | Ensure intelligence handling aligns with privacy laws | Phase 6, Phase 12 |
|  | Regulatory Bodies | Review reporting, breach notifications, and threat mitigation adherence | Phase 12 |
| Training & Awareness Audiences | Security Trainers / Educators | Teach staff how to use threat intelligence effectively | Phase 9, Phase 10 |
|  | Internal Staff & End Users | Improve awareness of phishing, social engineering, and threats | Phase 9, Phase 10 |
|  | Simulation & Gamification Participants | Engage with red/purple team exercises or SOC drills | Phase 7, Phase 10 |


---
## ✨ Key Features

<details>
<summary>1. Data Ingestion & Acquisition</summary>

- **Structured threat feeds:**
  - CVEs (NVD)
  - MITRE ATT&CK & CAPEC
  - ExploitDB
  - Internal vulnerability scans (Nessus, Qualys)
  - STIX/TAXII feeds from TIPs
- **Unstructured threat sources:**
  - Security reports, blogs, whitepapers
  - APT notes
  - Paste sites, leak hubs, social media
- Dark web & underground monitoring (optional, compliance-aware)
- Threat intelligence communities (MISP, AlienVault OTX, Open Threat Exchange)
- Automated ingestion pipelines with scheduling & retry mechanisms
- Data deduplication, validation, and integrity checks

</details>

<details>
<summary>2. Data Normalization & Enrichment</summary>

- Standardization of fields across multiple sources
- Deduplication and canonicalization of IOCs, TTPs, vulnerabilities
- **Context enrichment:**
  - VirusTotal, Shodan, Passive DNS
  - Cloud asset inventories (AWS, Azure, GCP)
  - Internal asset CMDB
  - Network and endpoint telemetry
- Historical tracking & versioning of CVEs/IOCs
- Mapping to organizational context (asset criticality, business tags)

</details>

<details>
<summary>3. AI & Analytics Features</summary>

- **Context-aware risk scoring:**
  - Multi-factor vulnerability scoring (CVSS, EPSS, KEV, asset criticality, exposure)
  - Stakeholder-specific scoring (SSVC)
  - Organizational risk matrices
- Attack path simulation & probability estimation
- Monte Carlo and “what-if” simulations for mitigation planning
- **Threat correlation:**
  - Campaign & adversary behavior analysis
  - TTP chaining
  - Cross-source intelligence fusion
- **Anomaly Detection & Proactive Alerts:**
  - ML/statistical anomaly detection on vuln/asset patterns
  - Unusual lateral movement detection
  - Deviations from normal attack paths
  - Correlation with historical baselines & external intel
- Continuous learning & feedback loop for AI models
- **NLP-based graph querying:**
  - Natural language questions
  - Contextual answers and recommendations
- Predictive modeling for exploit likelihood and risk propagation

</details>

<details>
<summary>4. Automation & Orchestration</summary>

- Remediation playbook generation (SOAR-ready)
- Integration with ITSM/SIEM/SOAR platforms:
  - Splunk, Jira, ServiceNow
- Automated ticket creation and workflow assignment
- Prioritized patching & mitigation recommendations
- Auto-upgrade of asset risk based on exposure
- Integration with alerting & notification systems
- Pipeline orchestration with Airflow/Kafka microservices

</details>

<details>
<summary>5. Visualization & Dashboards</summary>

- Interactive dashboards for:
  - Asset risk posture
  - Vulnerability prioritization
  - Attack path simulations
  - Anomaly alerts
  - Campaign & TTP correlations
- Trend analysis & KPI monitoring
- Drill-down reporting for analysts and executives
- Customizable dashboards per role (SOC analyst, CISO, IT manager)

</details>

<details>
<summary>6. Collaboration & Threat Sharing</summary>

- STIX/TAXII export/import
- Integration with TIPs & community sharing platforms
- Annotate and comment on incidents or campaigns
- Collaborative dashboards for teams
- Versioned threat intelligence sharing

</details>

<details>
<summary>7. Security & Compliance</summary>

- Role-Based Access Control (RBAC)
- Audit logging for all actions
- GDPR, CCPA, ISO27001 compliance considerations
- Data encryption at rest & in transit
- Credential handling best practices

</details>

<details>
<summary>8. Monitoring & Observability</summary>

- **Metrics collection:**
  - % critical vulns covered by playbooks
  - Average attack path length
  - SLA adherence
  - Anomaly counts per period
- Real-time alerting for critical changes
- Feedback loops for analysts
- Continuous improvement pipelines for ML/AI scoring

</details>

<details>
<summary>9. Developer & Extensibility Features</summary>

- REST API endpoints for:
  - Querying vulnerabilities, assets, TTPs, campaigns
  - Retrieving risk scores, simulations, and alerts
- Plugin or microservice-based architecture
- Versioned schema updates
- Documentation and examples for integration

</details>



## 🏗 Architecture
Detailed diagrams and explanation of the system components, data flow, integrations, and deployment environment. Include CI/CD and modular architecture if relevant.

## 💻 Installation
Step-by-step instructions to set up the environment, install dependencies, configure databases, and run the CTI-KG platform locally or in the cloud.

## 🔧 Configuration
How to configure API keys, credentials, pipeline parameters, environment variables, logging levels, and other operational settings.



## 🧠 Malwatch Pipeline Phases
: Full Inputs & Outputs & The Inbetweens (INPUTS AND OUTPUTS OF EACH PHASE NEEDS TO BE REVISED REALLY HARD)

The following sections detail each phase of the **Malwatch Pipeline**, including **inputs, internal processing, outputs**, and how they **connect to other phases**. This aligns directly with the agenda outlined in the Table of Contents.




<details> 
  <summary>✅ Phase 1: Threat Data Acquisition and Ingestion</summary> 

### 🔁 Inputs:
- **NVD API keys** → Primary CVE feed for vulnerabilities (2002–present).  
- **MITRE ATT&CK & CAPEC repos** → TTPs, attack patterns, and adversary behaviors.  
- **ExploitDB archives** → Exploit proofs-of-concept (PoCs).  
- **Organization’s cloud/infrastructure credentials** → AWS, Azure, GCP asset inventories (EC2, S3, IAM roles, etc.).  
- **Vulnerability scanner (Nessus/Qualys) access** → Internal vulnerability scan results.  
- **Dark web & underground forums monitoring feeds (optional, compliance-dependent)** → Credentials, chatter, malware sales.  
- **Public YARA & Sigma repositories** → Rules for malware detection and log correlation.  
- **Threat intelligence sharing communities (MISP, AlienVault OTX, Open Threat Exchange)** → Extra IOC feeds.  
- **Exploit weaponization trackers (CISA KEV, Exploit Prediction Scoring System - EPSS)** → Real-world exploitation signals.  
- **Paste sites & leak hubs (Pastebin, GitHub gists, Telegram dumps)** → Stolen credentials, config leaks.  

---

### ⚙️ Inside (Collection & Ingestion):
- Fetch daily CVE updates via NVD API (including modified feeds for historical corrections).  
- Sync ATT&CK/CAPEC knowledge bases weekly to catch new/updated TTPs.  
- Scrape ExploitDB & GitHub repos for new PoCs.  
- Pull cloud asset inventories (AWS Config, Azure Resource Graph, GCP Cloud Asset Inventory).  
- Run vulnerability scans (Nessus/Qualys/Cloud-native scanners like AWS Inspector).  
- Ingest YARA/Sigma rules for threat detection mapping to logs/telemetry.  
- Collect leak/breach exposure data (credentials, API keys, tokens) from commercial + OSINT breach monitoring services.  
- Subscribe to exploit weaponization feeds (EPSS API, CISA KEV catalog).  
- Collect OSINT domain/IP blacklists (Abuse.ch, Spamhaus, PhishTank).  
- Apply deduplication & tagging at ingestion (marking each record with source + timestamp + confidence).  
- Store everything in raw data lake (Bronze layer) for replay and auditing.  

---

### 🏗️ Storage & Infra Blueprint:
- **CVE Data (NVD JSON feeds)** → Raw JSON in object store (S3, Azure Blob, HDFS). Indexed in Elasticsearch/OpenSearch for fast lookup.  
- **ATT&CK & CAPEC repos** → Version-controlled in Git + object storage. Synced into Graph DB (Neo4j/JanusGraph) during KG construction.  
- **ExploitDB & PoCs** → JSON/Markdown archives in S3/HDFS. Indexed in code search DB (Elasticsearch + embeddings for semantic search).  
- **Cloud asset inventories** → Stored in relational DB (Postgres/CloudSQL) for structured querying + mirrored in object store for historical snapshots.  
- **Vulnerability scanner outputs** → Stored in Postgres for structured joins with assets. Also exported to Parquet in S3 for analytics.  
- **IOCs (IPs/domains/hashes)** → Written into time-series DB (InfluxDB, TimescaleDB, OpenSearch) for historical tracking & correlation.  
- **YARA/Sigma rules** → Stored in Git-based repo + object store for reproducibility. Loaded into SIEM / search engines for live use.  
- **Dark web / leaks** → Encrypted JSON in object store. Indexed in Elasticsearch for analyst search.  
- **Exploit weaponization feeds (EPSS/KEV)** → Cached in Postgres for fast scoring joins with CVEs.  
- **All raw feeds** → Land in Bronze (raw) layer of Medallion architecture (S3/HDFS + Delta Lake). ETL jobs promote to Silver (normalized) → Gold (curated/KG).  

---

### 🔄 Pipeline Orchestration & Automation:
- **Workflow Orchestration:**  
  - Use Apache Airflow or Prefect for DAG scheduling (daily CVEs, weekly ATT&CK syncs, hourly IOC updates).  
  - Each source mapped to a DAG task with retries + backoff (e.g., NVD API → retry up to 3x with exponential delay).  

- **Streaming & Event Handling:**  
  - Use Kafka (or AWS Kinesis / GCP PubSub) for real-time feeds (dark web leaks, IOC streams, scanner deltas).  
  - Producers: Scrapers & API collectors.  
  - Consumers: Storage writers (object store, DB, search index).  

- **Data Flow:**  
  1. Fetch → APIs, scrapers, scanners.  
  2. Queue → Kafka topic (e.g., `cves.raw`, `iocs.raw`, `cloud.assets`).  
  3. Transform → Lightweight parsing & tagging.  
  4. Store → Write to raw Bronze layer (object store / DB).  
  5. Index → Push structured fields to Elasticsearch/Neo4j/timeseries DB.  

- **Monitoring & Observability:**  
  - Metrics pushed to Prometheus/Grafana (data freshness, ingestion lag, failed jobs).  
  - Logs centralized in ELK / OpenSearch.  
  - Alerts on data staleness (e.g., “No CVE updates in 24h”).  

- **Resilience:**  
  - Dead-letter queues (DLQ) in Kafka for bad events.  
  - Retry policies for transient failures (e.g., 404/500 from feeds).  
  - Backpressure handling to avoid DB overload.  

---

### 🎯 Purpose:
Build a repeatable, resilient, and observable collection system that continuously ingests structured & unstructured threat intelligence into storage backends. Provides the raw foundation for enrichment, correlation, and KG construction.  

---

### 📤 Outputs:
- `/data/raw/cves.json` → Raw CVE data (with metadata).  
- `/data/raw/attack_patterns.csv` → ATT&CK & CAPEC attack techniques.  
- `/data/context/cloud_assets.json` → Organization’s cloud and internal infrastructure.  
- `/data/raw/exploits.json` → ExploitDB & GitHub PoCs.  
- `/data/raw/iocs.csv` → Collected IOCs (IPs, domains, hashes).  
- `/data/raw/breaches.json` → Exposed credentials/leaks.  
- `/infra/storage_map.md` → Living documentation of where each dataset is stored (object store, DB, time-series, graph, etc.).  
- `/infra/pipeline_orchestration.md` → DAGs, Kafka topics, retries, monitoring dashboards.  

🔁 **Used again in:** Phase 2, Phase 3, Phase 5  

</details>


<details> 
  <summary>✅ Phase 2: Data Normalization & Enrichment</summary> 

### 🔁 Inputs:
- Raw feeds from Phase 1 (CVE JSON, ATT&CK, Exploits, IOC lists, leaks, scanner outputs).  
- IOC enrichment APIs: Passive DNS, VirusTotal, AbuseIPDB, Whois, Shodan, GreyNoise.  
- Threat intelligence standards: STIX 2.1 / TAXII, CSAF (Common Security Advisory Framework).  
- Asset context from relational DB (cloud & internal inventories).  
- Threat scoring models: CVSS v3, EPSS, FIRST SSVC, custom risk scoring.  

---

### ⚙️ Inside (Transformation & Enrichment):

1. **Normalization & Schema Alignment:**  
   - Parse heterogeneous formats (JSON, CSV, XML, TXT dumps) → convert into a canonical schema (aligned with STIX 2.1 objects).  
   - Ensure fields are standardized:  
     - CVEs → `{CVE-ID, CPE, CAPEC, CVSSv3, EPSS, KEV}`  
     - IOCs → `{indicator type, value, first_seen, last_seen, source, confidence, TTL}`  
     - TTPs → `{ATT&CK Technique ID, Description, References}`  
   - Store canonical schema definition in `/infra/schemas/`.  

2. **Deduplication & Conflict Resolution:**  
   - Remove overlapping CVE records (e.g., NVD vs vendor advisories).  
   - Use fuzzy matching + hashes to collapse duplicate PoCs.  
   - Apply trust/confidence ranking per source (NVD > vendor > OSINT).  

3. **Enrichment Pipelines:**  
   - **CVE Enrichment:**  
     - Attach CVSS v3.1 base/temporal/environmental scores.  
     - Lookup EPSS probability (Exploit Prediction).  
     - Mark KEV (Known Exploited Vulnerability) if present.  
   - **IOC Enrichment:**  
     - IPs/domains → Passive DNS history, ASN, geolocation, hosting provider.  
     - Hashes → VirusTotal sample lookups, malware family classification.  
     - Domains → WHOIS info, DNSSEC status, expiration dates.  
     - IPs → GreyNoise tags (benign scanner vs malicious).  
   - **Threat Rule Enrichment:**  
     - YARA/Sigma rules → link back to malware families and ATT&CK techniques.  
   - **Asset Context:**  
     - Map CVEs to internal assets via CPE ↔ software inventory joins.  
     - Prioritize vulnerabilities by whether they appear in the org’s tech stack.  

4. **Prioritization & Scoring:**  
   - Apply FIRST SSVC (Stakeholder-Specific Vulnerability Categorization).  
   - Contextual scoring pipeline → base risk × exploitability × asset exposure × business impact.  
   - Generate composite **“Threat Score”** field.  

5. **Interoperability Transformation:**  
   - Export enriched bundles as STIX/TAXII 2.1 objects.  
   - CSAF advisory bundles for vulnerability disclosures.  
   - Normalized tables for joins in analytics (Parquet in `/data/silver/`).  

---

### 🏗️ Storage & Infra Blueprint:
- Normalized CVE, Exploit, TTPs: Stored in Delta Lake Silver layer (`/data/silver/cves.parquet`, `/data/silver/exploits.parquet`).  
- IOC time-series (with enrichments): Stored in TimescaleDB / InfluxDB for correlation queries.  
- STIX/TAXII Bundles: Versioned in object store (`/data/normalized/stix/`). TAXII server (OpenTAXII) serves enriched objects to downstream consumers.  
- Asset-context joins: Stored in relational DB (Postgres/CloudSQL) for queryable mappings.  
- Search index: Enriched CVE/IOC metadata indexed in Elasticsearch/OpenSearch for fast analyst queries.  
- Schemas & transformations: Version-controlled in Git repo (`/infra/schemas/`, `/infra/mappings/`).  

---

### 🔄 Pipeline Orchestration & Automation:
- **Airflow DAGs** to trigger enrichment after raw ingestion completes.  
- **Kafka topics (phase1.raw → phase2.normalized):**  
  - `cves.raw` → `cves.enriched`  
  - `iocs.raw` → `iocs.enriched`  
  - `assets.raw` → `assets.contextualized`  
- Parallel enrichment workers: Python microservices for CVE, IOC, TTP pipelines.  
- Dead-letter queues (DLQ): Failed enrichments → `phase2.errors` topic.  

---

### 📊 Monitoring & Observability:
- **Prometheus metrics:** enrichment success %, API latency (e.g., VirusTotal rate-limits), deduplication ratios.  
- **Grafana dashboards:** CVE coverage, IOC enrichment depth, source freshness.  
- **Alerts:** API quota exhaustion, enrichment pipeline lag, schema drift detection.  

---

### 🎯 Purpose:
- Convert raw heterogeneous feeds → clean, normalized, enriched intelligence.  
- Establish canonical representations in STIX/TAXII + Delta Lake Silver tables.  
- Provide enriched, deduplicated data ready for correlation, analytics, and KG ingestion.  

---

### 📤 Outputs:
- `/data/silver/*.parquet` → Normalized datasets (CVE, IOC, Exploits, TTPs).  
- `/data/normalized/stix/*.json` → Enriched STIX 2.1 bundles.  
- `/data/context/*.json` → Asset-context-mapped vulnerabilities.  
- `/indexes/opensearch/` → Fast analyst search.  
- `/infra/schema_map.md` → Canonical schema documentation.  
- `/infra/api_usage.md` → API quota & enrichment performance logs.  

🔁 **Used again in:** Phase 3 (Knowledge Graph Construction), Phase 5 (Correlation & Analytics).  

</details>


<details> <summary>✅ Phase 3: Unstructured Data Processing</summary> 

🔁 **Inputs:**  
- Threat Reports: Vendor advisories (PDF/HTML), CERT/CSIRT reports, industry whitepapers.  
- Security Blogs: FireEye/Mandiant, CrowdStrike, Recorded Future, etc.  
- APT Notes & Dark Web Leaks: Campaign writeups, paste sites, leaked notes.  
- Scanned Docs: Intelligence reports with embedded images, old PDF scans, or screenshots.  

⚙️ **Inside (Processing Pipeline):**  
1. **Ingestion & Preprocessing:**  
   - File acquisition (RSS feeds, crawlers, API pulls).  
   - Format conversion (PDF → text, HTML parsing, DOCX → text).  
   - **OCR Layer:**  
     - Apply Tesseract or AWS Textract on scanned PDFs/images.  
     - Extract embedded text/images → feed downstream NLP.  
   - Language detection (FastText/langid).  

2. **Text Normalization:**  
   - Remove boilerplate (ads, headers, footers).  
   - Sentence segmentation & tokenization.  
   - Stopword removal, stemming/lemmatization (multilingual).  
   - Encode metadata (source, timestamp, author, URL).  

3. **Entity Extraction (NER):**  
   - BERT-based NER models trained on CTI datasets.  
   - Extract structured entities:  
     - CVEs, CWEs, CAPEC IDs.  
     - ATT&CK Techniques (T####).  
     - IOCs (IP, domain, URL, hash).  
     - Malware/Tool names.  
     - Threat actor groups (APT29, FIN7).  
     - Victim sectors & geographies.  
   - Store raw entities in `/data/processed/extracted_entities.json`.  

4. **Contextual Relationship Extraction (LLMs):**  
   - Use GPT-4/Domain-tuned LLMs:  
     - Link extracted CVEs to exploits, malware families, or ATT&CK techniques.  
     - Infer “who–what–how” relationships (e.g., APT29 used Spearphishing (T1566) with CVE-2023-23397).  
     - Extract temporal indicators (attack campaign active 2021–2023).  
   - Output structured triples: **(Actor) –uses→ (Technique) –exploits→ (CVE).**  

5. **Multilingual NLP Support:**  
   - Models for Russian, Chinese, Farsi, Arabic → common in APT blogs & leaks.  
   - Parallel translation pipelines (MarianMT, DeepL API).  
   - Align multilingual entities → canonical English KG representation.  

6. **Embedding Generation:**  
   - Use sentence-transformers (SBERT) or OpenAI embeddings.  
   - Store embeddings in vector DB (FAISS, Milvus, Pinecone).  
   - Enables semantic search (find similar incidents or related reports).  

7. **Conversion to KG-Compatible Triples:**  
   - Map entities & relations → CTI-KG schema (from Phase 3).  
   - Example:  
     - Extracted text: *“APT41 exploited CVE-2021-44228 (Log4Shell) via T1190.”*  
     - Converted triple: **(APT41) –uses→ (T1190), (T1190) –exploits→ (CVE-2021-44228).**  
   - Deduplicate against existing KG nodes (avoid redundant CVEs or IOCs).  

8. **Human-in-the-Loop Validation:**  
   - Low-confidence extractions (e.g., ambiguous entity *"Zeus"* = Malware or Actor?).  
   - Analyst review UI.  
   - Feedback loop → fine-tune extraction models.  

🏗️ **Storage & Infra Blueprint:**  
- Raw Docs Storage: `/data/raw/unstructured/` (PDF/HTML).  
- Preprocessed Text: `/data/processed/text/`.  
- Entity JSON: `/data/processed/extracted_entities.json`.  
- Relationship Updates: `/data/processed/kg_updates/*.json`.  
- Embeddings: Stored in Milvus/FAISS for similarity search.  

🔄 **Pipeline Orchestration:**  
- Airflow DAG: `unstructured_pipeline_dag`.  
- Kafka topics:  
  - `phase4.raw_docs` → ingestion.  
  - `phase4.entities` → extracted NER.  
  - `phase4.kg_updates` → consumed by Phase 3 KG builder.  
- Microservices:  
  - `doc_ingestor` (fetch, store).  
  - `entity_extractor` (NER).  
  - `rel_inferencer` (LLM context builder).  
  - `embedding_service` (vector storage).  

📊 **Monitoring & Observability:**  
- Dashboards: #docs ingested/day, #entities extracted, NER precision/recall.  
- Alerts: OCR failures, extraction error spikes, unusual surges in malware mentions.  
- Drift detection: language distribution (e.g., sudden increase in Farsi sources).  

🎯 **Purpose:**  
- Transform unstructured threat intel into structured, KG-ready knowledge.  
- Enable semantic search, pattern discovery, and APT campaign correlation.  
- Support multilingual CTI coverage (Russian/Chinese threat actor blogs).  

📤 **Outputs:**  
- `/data/processed/extracted_entities.json` → structured entities.  
- `/data/processed/kg_updates/*.json` → triples for KG ingestion.  
- `/data/processed/embeddings/` → document & entity embeddings.  
- Updated KG nodes/edges in Phase 3 DB.  
- Vector DB embeddings → used in chatbot (Phase 6) and semantic search (Phase 9).  

🔁 **Used again in:**  
- Phase 3: Feeding relationship updates to KG.  
- Phase 6: Chatbot Q&A over threat reports.  
- Phase 9: Advanced analytics & semantic similarity detection.  

</details>



<details> <summary>✅ Phase 4: Threat Attribution & Campaign Correlation</summary> 

🔁 **Inputs:**
- KG entities (from Phase 3 & 4): CVEs, ATT&CK TTPs, IOCs, Malware, Infrastructure nodes.  
- External Campaign Databases:  
  - MISP Galaxy: threat actor & intrusion set mappings.  
  - MITRE ATT&CK Groups: APT groups & known TTPs.  
  - Threat Actor Wikis / CTI Vendor Reports (FireEye, CrowdStrike, Kaspersky).  
- OSINT Feeds: Pastebin, VirusTotal community intel, Shodan, Censys scans.  
- Attribution Metadata: Whois, SSL cert transparency logs, ASN/IP history.  

⚙️ **Inside (Processing Pipeline):**
1. **Entity Alignment & Normalization:**  
   - Map KG nodes (APT29, Cozy Bear, “APT 29”) → canonical group IDs (ATT&CK G0016).  
   - Normalize malware/tool aliases (“Cobalt Strike”, “Beacon”, “CS”) → unified node.  
   - Deduplicate infrastructure artifacts (same IP/domain across multiple feeds).  

2. **IOC & TTP → Threat Actor Linking:**  
   - Match extracted IOCs (IPs/domains/hashes) against known APT infrastructure datasets (MISP, ATT&CK).  
   - Correlate TTP usage (ATT&CK techniques) with group profiles.  
   - Confidence scoring: Bayesian model or weighted overlap (TTP similarity, infra reuse, malware overlap).  

3. **Campaign Correlation:**  
   - Identify clusters of activity by:  
     - Shared IOCs (same C2 servers, reused domains).  
     - Malware/tool overlaps (e.g., PlugX, Cobalt Strike).  
     - Exploited vulnerabilities (e.g., Log4Shell in multiple campaigns).  
   - Use graph algorithms:  
     - Community detection (Louvain, Leiden) on infrastructure subgraphs.  
     - Temporal correlation (e.g., activity peaks during elections).  

4. **Adversary Profile Construction:**  
   - Auto-generate profiles per actor:  
     - Infrastructure: IP ranges, hosting providers, SSL cert reuse.  
     - Toolset: malware families, exploit kits, loaders.  
     - TTP patterns: mapped ATT&CK techniques & procedures.  
     - Target sectors & geographies.  
   - Store as structured JSON + KG nodes.  

5. **Temporal Analysis:**  
   - Timeline view: campaign activity by month/year.  
   - Correlate exploit usage with disclosure dates (e.g., CVE-2023-23397 used within 7 days of patch).  
   - Detect campaign evolution (new malware added, infrastructure rotation).  

6. **Clustering & Similarity Detection:**  
   - Infrastructure similarity scoring:  
     - Shared IP ranges, domains, SSL certs.  
     - ASN overlaps (e.g., bulletproof hosting).  
   - Cluster similar campaigns into larger intrusion sets.  
   - Flag potential false flag operations (when multiple groups mimic each other).  

7. **Analyst-in-the-Loop Validation:**  
   - Analysts can review attributions with confidence levels.  
   - Manual override → correction feeds back into attribution ML models.  
   - Attribution “audit trail” for accountability.  

🏗️ **Storage & Infra Blueprint:**  
- Attribution Results: `/data/attribution/campaign_links.json` (edges between campaigns, groups, and IOCs).  
- Adversary Profiles: `/data/attribution/profiles/{group_id}.json`.  
- Temporal Campaign Graphs: `/data/attribution/timelines/`.  
- GraphDB Updates: New nodes: Groups, Campaigns; New edges: “uses”, “targets”, “controls”.  

🔄 **Pipeline Orchestration:**  
- Airflow DAG: `attribution_pipeline_dag`.  
- Kafka topics:  
  - `phase5.attribution_links` → campaign correlations.  
  - `phase5.adversary_profiles` → per-group enriched nodes.  
- Microservices:  
  - `ioc_actor_matcher` (link IOCs ↔ APT groups).  
  - `campaign_clusterer` (graph community detection).  
  - `profile_builder` (adversary profile generation).  

📊 **Monitoring & Observability:**  
- Attribution confidence distribution (low/medium/high).  
- Campaign cluster count (growth/shrink over time).  
- Infra reuse metrics (domains/IPs seen across groups).  
- Alerts for “new APT campaign detected” when novel clusters appear.  

🎯 **Purpose:**  
- Provide contextual intelligence: who is behind which campaigns, what vulnerabilities they use, when they are active, and who they target.  
- Build adversary-centric knowledge (APT profiles, campaign timelines).  
- Enhance situational awareness for defenders & analysts.  

📤 **Outputs:**  
- `/data/attribution/campaign_links.json` → campaign ↔ actor ↔ IOC relations.  
- `/data/attribution/profiles/*.json` → adversary profiles.  
- New Group-level KG nodes & edges (e.g., APT29 –uses→ T1566 –exploits→ CVE-2023-23397).  
- Temporal campaign datasets for visualization dashboards.  

🔁 **Used again in:**  
- **Phase 6 (Chatbot & Q&A):** Answer “Which groups are exploiting Log4Shell?”  
- **Phase 7 (Attack Path Simulation):** Use real campaign data to simulate attack chains.  

</details>


<details> 
  <summary>✅ Phase 5: Context-Aware Analysis & Anomaly Detection</summary> 

🔁 **Inputs:**
- Knowledge Graph state (Phase 3–5): vulnerabilities, TTPs, IOCs, campaign links.  
- Org asset inventory: CMDB, cloud workloads, containers, endpoints, SaaS apps.  
- Business context tags: criticality levels (e.g., “Tier-0 DCs”, “Finance systems”, “Customer data stores”).  
- External exposure data: breach/leak databases, credential dumps, dark web monitoring.  

⚙️ **Inside (Processing Pipeline):**
1. **Vulnerability Scoring with Context:**  
   - Combine CVSS v3.1, EPSS (likelihood of exploitation), KEV (CISA Known Exploited Vulnerabilities) with:  
     - Asset criticality (crown jewels vs test systems).  
     - Exposure state (internet-facing vs internal).  
     - Compensating controls (WAF, EDR, MFA presence).  
   - Apply multi-factor scoring models:  
     - FIRST SSVC (Stakeholder-Specific Vulnerability Categorization).  
     - Custom org risk matrices.  
   - **Output = prioritized risk score per vuln/asset pair.**

2. **Attack Path Simulation:**  
   - Use KG graph traversal (Neo4j queries):  
     - Find paths like `External Asset → CVE Exploit → Lateral Movement → Domain Admin`.  
   - Integrate ATT&CK TTP chaining: model how a vuln leads to persistence, privilege escalation, data exfil.  
   - Assign probabilities based on adversary campaign intelligence (from Phase 5).  

3. **What-If & Decision Simulation:**  
   - Simulate outcomes:  
     - “If CVE-2023-23397 is patched → attack path X is broken.”  
     - “If left unpatched → reachable crown jewels within 3 steps.”  
   - Run Monte Carlo attack simulations for likelihood estimation.  
   - Suggest alternative mitigations (segmentation, compensating controls).  

4. **Remediation Planning:**  
   - Auto-generate ranked remediation actions:  
     - Patching critical vulns on Tier-0 first.  
     - Credential reset if exposed in breach datasets.  
     - Infra hardening (RDP disable, SMBv1 disable).  
   - Map remediation to playbooks (SOAR integrations).  
   - Include effort vs impact scoring (low effort, high impact patches prioritized).  

5. **Exposure Checks & Credential Correlation:**  
   - Check if org domains/emails appear in breach data.  
   - Map exposed creds to AD accounts, SaaS logins, VPNs.  
   - Correlate with asset inventory → highlight vulnerable access paths.  
   - Trigger auto-risk upgrade for assets tied to leaked creds.  


6. **Anomaly Detection & Proactive Alerts** 🔍
   - **Inputs:** current KG state, attack path simulations, asset exposures, historical risk baselines, external threat intel.
   - **Processing:**
     - ML/statistical anomaly detection on vuln/asset patterns.
     - Detect unusual activity or deviations from normal attack paths.
     - Correlate anomalies with TTPs or known adversary campaigns.
   - **Outputs:**
     - `/reports/anomaly_alerts.json` → flagged anomalies.
     - Updated priority scores for assets/vulnerabilities.
     - Alerts fed into dashboards, analyst reviews, or automated SOAR playbooks.

7. **Analyst-in-the-Loop Enhancements:**  
   - Analyst dashboards to review risk scoring explanations (why is this vuln critical?).  
   - Feedback loop to adjust risk models (e.g., CFO system tagged higher priority).  
   - ML-based continuous tuning of context scoring weights.  

🏗️ **Storage & Infra Blueprint:**
- Priority Alerts: `/reports/priority_alerts.json`.  
- Remediation Plans: `/reports/remediation_playbooks/*.json`.  
- Splunk/Jira Alerts: via REST/webhook integration.  
- Attack Path Graphs: `/data/simulation/attack_paths/*.graphml`.  

🔄 **Pipeline Orchestration:**
- Airflow DAG: `context_analysis_pipeline_dag`.  
- Kafka topics:  
  - `phase6.priority_scores` → vuln/asset risk scoring.  
  - `phase6.attack_paths` → simulated paths.  
  - `phase6.remediation` → playbook generation.
  - `phase6.anomalies` → anomaly detection & alerts.
- Microservices:  
  - `vuln_risk_scorer` (CVSS+EPSS+context).  
  - `attack_path_simulator` (Neo4j graph traversals).  
  - `remediation_generator` (playbook builder).  
  - `breach_exposure_checker` (credential correlation).
  - `anomaly_detector` (ML/statistical anomaly scoring).

📊 **Monitoring & Observability:**
- **Metrics:**  
  - % of critical vulns covered by playbooks.  
  - Avg attack path length to Tier-0.  
  - % of org assets tied to breach exposures.  
  - SLA adherence for remediation tasks.  
- **Alerting:**  
  - “Crown jewel exposed via single-step exploit!”  
  - “New KEV vuln detected on internet-facing asset.”
  - “Unusual lateral movement detected on finance assets.”

🎯 **Purpose:**
- Turn raw threat data into actionable, business-aware intelligence.  
- Provide org-specific risk context (not all CVEs matter equally).  
- Enable data-driven prioritization of patching and mitigation.  
- Support executive reporting (risk posture, trending attack paths).
- Detect anomalous activity proactively and trigger alerts for rapid remediation.

📤 **Outputs:**
- `/reports/priority_alerts.json` → top-risk vulnerabilities & assets.
- `/reports/anomaly_alerts.json` → flagged anomalies for analyst review.
- Splunk/Jira/ServiceNow tickets → automated remediation workflows.  
- Recommended playbooks (SOAR-ready).  
- Simulation datasets → attack path visualizations for analysts.  

🔁 **Used again in:**
- **Phase 7 (Attack Path Simulation & Red Teaming):** uses scoring + simulations.  
- **Phase 8 (Automated Defense & SOAR):** consumes remediation playbooks.  

</details>



<details> <summary>✅ Phase 6: Adversary Simulation & Hunting Prep</summary> 

🔁 **Inputs:**
- Knowledge Graph with attack paths (Phase 6): simulated exploitation chains, vulnerable assets, lateral movement routes.  
- ATT&CK techniques & sub-techniques: official ATT&CK Enterprise & Cloud matrices.  
- Threat attribution data (Phase 5): APT groups, malware families, infrastructure fingerprints.  
- Org detection stack inventory: SIEM, EDR, NDR, cloud-native logs (Defender, GuardDuty, etc.).  

⚙️ **Inside (Processing Pipeline):**  
1. **Adversary Emulation Plan Generation:**  
   - Take active attack paths from Phase 6 → generate emulation scenarios.  
   - Tools integrated:  
     - Atomic Red Team (individual ATT&CK technique tests).  
     - MITRE Caldera (automated adversary emulation).  
     - Infection Monkey / Stratus Red Team (cloud-specific scenarios).  
   - Customize adversary profiles based on Phase 5 attribution (e.g., FIN7 vs APT29).  

2. **Detection Engineering & Query Export:**  
   - Map adversary actions → log sources (Windows Event Logs, Sysmon, Zeek, EDR telemetry).  
   - Auto-generate Sigma rules, then convert to:  
     - Splunk SPL  
     - Elastic KQL  
     - Sentinel KQL  
     - QRadar AQL  
   - Ensure coverage for emulated techniques → deliver ready-to-run hunting queries.  

3. **ATT&CK Coverage Matrix Mapping:**  
   - Maintain org-specific coverage heatmap:  
     - Which techniques are detected (green).  
     - Which are partially detected (yellow).  
     - Which have no coverage (red).  
   - Use mitigations + detections to highlight gaps.  
   - Export as JSON + interactive dashboards.  

4. **Purple Team & Threat Hunting Prep:**  
   - Create adversary simulation playbooks (step-by-step TTP execution).  
   - Export detection queries + playbooks → `/hunts/queries/*.yml`.  
   - Align with threat hunting cycles (hypothesis-driven hunts).  
   - Build hunt packages:  
     - Scenario description (adversary, TTPs).  
     - Detection queries.  
     - Expected artifacts/log sources.  
     - ATT&CK mapping.  

5. **Continuous Feedback Loop:**  
   - Feed back simulation results into KG:  
     - “Detection success = ✅”  
     - “Detection failure = ❌ → gap flagged”  
   - Analysts validate effectiveness of detections.  
   - Update hunt library and refine queries based on SOC feedback.  

🏗️ **Storage & Infra Blueprint:**  
- Hunting Queries: `/hunts/queries/*.yml` (Sigma + native SIEM queries).  
- ATT&CK Coverage Reports: `/reports/attack_coverage/*.json`.  
- Simulation Playbooks: `/hunts/playbooks/*.md`.  
- Gap Tracking DB: `/data/detection_gaps.sqlite`.  

🔄 **Pipeline Orchestration:**  
- Airflow DAG: `adversary_simulation_pipeline_dag`.  
- Kafka topics:  
  - `phase7.emulation_plans` → Atomic/Caldera jobs.  
  - `phase7.detection_queries` → Sigma → SIEM export.  
  - `phase7.coverage_reports` → ATT&CK heatmaps.  
- Microservices:  
  - `emulation_plan_generator`  
  - `detection_query_builder`  
  - `coverage_mapper`  
  - `hunt_package_creator`  

📊 **Monitoring & Observability:**  
- **Metrics:**  
  - % of ATT&CK techniques covered by detection.  
  - # of adversary scenarios executed/month.  
  - Detection gap reduction over time.  
  - MTTD (Mean Time to Detect) improvement after hunts.  
- **Alerting:**  
  - “New APT campaign detected but no coverage for T1059 (Command Execution).”  
  - “Sigma rule failed to execute in Splunk.”  

🎯 **Purpose:**  
- Empower purple teams (red + blue) with realistic adversary playbooks.  
- Provide threat hunters with hypothesis-driven queries mapped to ATT&CK.  
- Continuously measure and close detection coverage gaps.  
- Ensure org defenses evolve alongside adversary TTPs.  

📤 **Outputs:**  
- `/hunts/queries/*.yml` → ready-to-run hunting rules.  
- ATT&CK coverage reports (JSON + dashboards).  
- Adversary simulation playbooks (Caldera/Atomic packages).  
- Gap analysis datasets → feed Phase 8 defense automation.  

🔁 **Used again in:**  
- Phase 8 (Automated Defense & SOAR): consumes playbooks + queries.  
- Phase 9 (Interactive Analyst Interfaces): exposes coverage reports & hunts to SOC teams.  

</details>




<details> <summary>✅ Phase 7: Automation & Integration</summary> 

🔁 **Inputs:**
- Analysis results (Phase 6): prioritized alerts, attack paths, remediation recommendations.  
- Hunt/simulation outputs (Phase 7): detection queries, adversary simulation results, coverage gaps.  
- SIEM/SOAR/ticketing credentials: Splunk, Sentinel, QRadar, ServiceNow, Jira, Slack, Teams.  
- Org-specific playbooks & policies: approved remediation workflows, escalation policies.  

⚙️ **Inside (Processing Pipeline):**  
1. **SIEM Alert Enrichment:**  
   - Take raw SIEM alerts → contextualize with KG knowledge:  
     - Map CVE → affected asset → known campaigns.  
     - Enrich IOC with threat actor attribution, malware family, campaign timelines.  
   - Add business context: asset criticality, exposure level, previous incidents.  
   - Store enriched alerts in `/alerts/enriched/*.json`.  

2. **Automated Remediation Ticketing:**  
   - Create remediation tasks in Jira/ServiceNow based on severity + asset owner.  
   - Auto-assign tickets using org asset inventory & ownership mapping.  
   - Include recommended remediation steps: patch KB link, firewall rule, EDR action.  
   - Track SLA compliance (critical vulns must be closed in X days).  

3. **SOAR Workflow Triggering:**  
   - Map enriched alerts → SOAR playbooks (e.g., Phantom, XSOAR, Shuffle).  
   - Example playbooks:  
     - Contain endpoint → isolate host in EDR.  
     - Block domain/IP → push to firewall/DNS sinkhole.  
     - Quarantine email → Exchange/Google Workspace.  
   - Trigger workflows automatically when confidence > threshold, or semi-auto with analyst approval.  

4. **Closed-Loop Feedback into KG:**  
   - Every enriched alert, ticket, and SOAR action → pushed back to KG:  
     - “Alert validated = ✅ / false positive = ❌”  
     - “Ticket closed = patched on host X”  
     - “Playbook executed = blocked domain, case closed”  
   - Update confidence scores of rules, enrichers, and models (reinforcement learning).  

5. **Collaboration & Notifications:**  
   - Send updates to analysts & stakeholders via:  
     - Slack/Teams for instant notifications.  
     - Email digests for daily summaries.  
     - Dashboards in Kibana/Grafana for monitoring metrics.  
   - Highlight critical incidents in executive view dashboards.  

6. **Automation Safeguards:**  
   - Built-in approval gates for destructive actions (e.g., mass endpoint isolation).  
   - Audit trail logging → every automated action logged for compliance.  
   - Rollback workflows (undo firewall block, restore host connectivity).  

🏗️ **Storage & Infra Blueprint:**  
- Enriched Alerts: `/alerts/enriched/*.json`.  
- Remediation Tickets DB: `/data/tickets.sqlite`.  
- SOAR Logs: `/data/soar_executions.log`.  
- Feedback DB: `/data/closed_loop_feedback.sqlite`.  

🔄 **Pipeline Orchestration:**  
- Airflow DAG: `automation_integration_pipeline_dag`.  
- Kafka topics:  
  - `phase8.enriched_alerts` → SIEM enrichment service.  
  - `phase8.remediation_tickets` → Jira/ServiceNow connector.  
  - `phase8.soar_actions` → SOAR execution service.  
  - `phase8.feedback_loop` → KG updater.  
- Microservices:  
  - `siem_enrichment_service`  
  - `ticketing_connector`  
  - `soar_executor`  
  - `feedback_integrator`  

📊 **Monitoring & Observability:**  
- **Metrics:**  
  - Avg. time to enrich SIEM alert.  
  - # of automated tickets created.  
  - # of SOAR playbooks executed (success vs failed).  
  - SLA compliance rate for remediation tasks.  
- **Alerting:**  
  - “Playbook execution failed on endpoint X.”  
  - “Remediation ticket overdue by >7 days.”  

🎯 **Purpose:**  
- Operationalize intelligence → ensure insights from KG + hunts result in real-world defense actions.  
- Automate response → reduce MTTR (Mean Time to Respond).  
- Enable closed-loop learning → system improves detection, enrichment, and playbooks over time.  
- Bridge intel → SOC → IT/Ops teams through automation and seamless integration.  

📤 **Outputs:**  
- SIEM Alerts (enriched): `/alerts/enriched/*.json`.  
- SOAR Playbook Executions: `/data/soar_executions.log`.  
- Remediation Tickets: Jira/ServiceNow/Slack/Teams notifications.  
- Feedback Reports: closed-loop enrichment logs.  

🔁 **Used again in:**  
- **Continuous Monitoring Cycle (Phases 9–12):**  
  - Phase 9 → Analyst Interfaces: SOC teams visualize enriched alerts.  
  - Phase 10 → Knowledge Fusion: feedback loop strengthens KG.  
  - Phase 11 → Reporting & Compliance: SLA metrics, audit trails.  
  - Phase 12 → Continuous Retraining: ML/LLMs improve based on action outcomes.  

</details>



<details> <summary>✅ Phase 8: Visualization & Analyst Workbench</summary> 

🔁 **Inputs:**
- KG snapshot: current graph of entities (CVEs, IOCs, campaigns, adversaries, assets).  
- Attack path analysis (Phase 6): prioritized attack chains, “what-if” outcomes.  
- Attribution data (Phase 5): APT groups, malware families, infrastructure clusters.  
- Automation feedback (Phase 8): enriched alerts, remediation tickets, playbook actions.  

⚙️ **Inside (Processing & UI Components):**  
1. **Graph Visualization Dashboards:**  
   - Interactive visual graph explorer with Neo4j Bloom, Graphistry, Cytoscape, or D3.js.  
   - Entities (nodes): CVEs, CWEs, assets, IOCs, APT groups, campaigns.  
   - Relationships (edges): “exploits,” “attributed_to,” “affects_asset,” “detected_by.”  
   - Color coding: vulnerabilities (red), assets (blue), adversaries (orange), detections (green).  
   - Edge weight: confidence level, frequency, temporal recency.  

2. **Timeline Explorer (Adversary Campaigns):**  
   - Show temporal evolution of campaigns (who attacked what, when).  
   - Sliding time bar to replay campaigns across months/years.  
   - Correlate new CVEs with historic campaigns for trend analysis.  

3. **Attack Path Simulation View:**  
   - Render attack graph traversal generated in Phase 6.  
   - Highlight critical nodes (“choke points” or crown jewels) where multiple paths converge.  
   - Interactive toggling: simulate “patched/unpatched” state to see updated path.  
   - Export to PDF/PNG for executive reporting.  

4. **Analyst Exploration UI:**  
   - Search bar with natural language + structured queries:  
     - “Show me all CVEs exploited by APT28 affecting our finance servers.”  
   - Drill-down view: click a node → expand related entities, supporting intel.  
   - Filters: by MITRE ATT&CK tactic, by asset type, by CVSS score, by campaign.  
   - Export queries into reusable hunt templates (feeds Phase 7).  

5. **Attack Surface Dashboards:**  
   - Combine external exposures (Shodan scans, DNS leaks, SSL certs) with internal assets (CMDB).  
   - Provide heatmaps of most exposed business units.  
   - Track open vulnerabilities per business function (finance, HR, R&D).  
   - Compare external view vs. internal inventory to catch blind spots.  

6. **Contextual Layers & Overlays:**  
   - Overlay geolocation maps (adversary infra, hosting providers).  
   - Integrate threat actor motivations (espionage, financial, disruptive).  
   - Show confidence scores for attribution links.  
   - Allow toggle between “tactical view” (IOCs, signatures) vs “strategic view” (actor trends).  

7. **Collaboration Features:**  
   - Analysts can annotate nodes/edges with comments or hypotheses.  
   - Share saved views/dashboards with teammates.  
   - Attach enrichment notes (e.g., PDF threat report snippet linked to node).  
   - Audit trail of who made annotations (useful for knowledge curation).  

8. **Infra & Storage:**  
   - UI endpoints: `/ui/visual_graph/`, `/ui/timeline/`, `/ui/attack_surface/`.  
   - Graph DB (Neo4j/ArangoDB) powers the visualizations.  
   - Cache: pre-rendered visualizations stored as JSON in `/data/viz_cache/`.  
   - API endpoints: `/api/viz/search`, `/api/viz/attack_paths`, `/api/viz/campaigns`.  

📊 **Monitoring & Metrics:**  
- Time-to-answer: avg time for analysts to resolve an intel query.  
- Query coverage: % of alerts/enriched entities visualized.  
- Analyst engagement: # of saved views, annotations, shared dashboards.  
- Performance: graph query response times (<1s for common queries).  

🎯 **Purpose:**  
- Give analysts superpowers: intuitive graph exploration beyond raw logs.  
- Turn intel into insights: see campaigns, attack paths, exposures visually.  
- Bridge SOC ↔ Threat Intel teams: common interactive workspace.  
- Support executive reporting: visual narratives for board/CISO.  

📤 **Outputs:**  
- Analyst Dashboards: `/ui/visual_graph/`, `/ui/timeline/`, `/ui/attack_surface/`.  
- Saved Views/Exports: `/reports/viz_exports/*.pdf|.png|.json`.  
- Annotations & Analyst Notes: `/data/annotations/*.json`.  
- Coverage Maps: ATT&CK matrix overlays.  

🔁 **Used again in:**  
- Phase 10 → Chatbot Explanations: chatbot uses visual graphs as context for narrative answers.  
- Phase 12 → Feedback & Retraining: analyst annotations refine entity extraction & attribution models.  
- Continuous Monitoring: dashboards auto-refresh with each KG update.  

</details>




<details> <summary>✅ Phase 9: NLP Chatbot Interface</summary> 

🔁 **Inputs:**
- User Queries: free-text analyst/SOC operator inputs (Slack, Teams, Web UI, CLI).  
- KG State: structured graph entities & relationships (CVE, TTP, IOCs, assets, campaigns).  
- Document Embeddings (Phase 4): unstructured threat reports, OSINT, advisories.  
- Conversation History: context from ongoing sessions for continuity.  

⚙️ **Inside (Processing & Dialogue Pipeline):**  
1. **Interface Layer (Multi-Channel Support):**  
   - Web UI: `/ui/chat/`.  
   - Integrations: Slack bot, MS Teams app, SOC chat console.  
   - CLI/terminal interface for threat hunters.  
   - REST API: `/api/chatbot/query`.  

2. **Preprocessing & Intent Classification:**  
   - Detect query type:  
     - 🔍 Fact Retrieval: “Which CVEs affect Apache Tomcat 9?”  
     - 📈 Trend Analysis: “Show campaigns exploiting Log4Shell in 2023.”  
     - 🛡 Defensive Guidance: “How do we mitigate CVE-2024-12345?”  
     - 👥 Actor Attribution: “Which APT groups are linked to this IOC?”  
   - Intent models: fine-tuned BERT/DistilBERT or GPT classifier.  
   - Entity extraction: NER to detect CVEs, MITRE ATT&CK TTPs, malware names, IPs/domains.  

3. **Query Translation (NL → KG + Docs):**  
   - Convert NL query → Cypher/Gremlin query for the KG.  
   - Augment with document retrieval using embeddings (FAISS, Milvus, Weaviate).  
   - Hybrid answer: structured KG + unstructured context.  

4. **Retrieval-Augmented Generation (RAG):**  
   - KG provides precise entities/links.  
   - Embeddings fetch unstructured text (advisories, PDFs, OSINT).  
   - Fusion: combine into a contextual package.  
   - Response generation with LLM (GPT/Jurassic/Mistral).  

5. **Response Generation:**  
   - Structured → narrative explanation (simplified or technical, depending on role).  
   - Summarization: collapse multiple docs into concise answer.  
   - Visual references: insert graph/timeline links (`/ui/visual_graph/?q=...`).  
   - Multi-tone support:  
     - Analyst mode (detailed, technical).  
     - Executive mode (summary, risk impact).  

6. **Feedback Logging & Learning:**  
   - Capture 👍/👎 feedback from analysts on responses.  
   - Store Q&A pairs in `/logs/chat_sessions.json`.  
   - Misunderstood queries flagged for intent retraining.  
   - Analyst-added clarifications become training examples (Phase 12 loop).  

7. **Security & Governance:**  
   - Role-based access: certain queries (e.g., “dump IOC feeds”) restricted to senior roles.  
   - PII/sensitive data redaction before storage.  
   - Audit logs of who asked what, when, and what answer was given.  

📊 **Monitoring & Metrics:**  
- Query success rate (% of questions answered with KG+Docs).  
- Response latency (target < 2s for KG-only, <5s for KG+Doc fusion).  
- Coverage: % of KG entities accessed via chatbot vs dashboards.  
- Analyst satisfaction: feedback ratio, session reuse.  

🎯 **Purpose:**  
- Enable natural-language access to complex CTI knowledge.  
- Reduce analyst workload (no need to write Cypher/SQL).  
- Bridge human + machine intelligence with RAG answers.  
- Provide interactive explanation layer before automation (Phases 8–9).  

📤 **Outputs:**  
- Chat Responses: delivered in Slack/Teams/Web UI.  
- Session Logs: `/logs/chat_sessions.json`.  
- Training Data: `/data/chatbot/training_samples.json`.  
- Linked Insights: auto-generated queries feeding Phase 9 visualizations.  

🔁 **Used again in:**  
- Phase 12 (Feedback Loop): retrain intent models & embeddings using session logs.  
- Phase 9 (Visualization): chatbot inserts deep-links to graph/timeline dashboards.  
- Continuous Monitoring: chatbot proactively alerts users (“New CVE matches your assets”).  

</details>


<details> <summary>✅ Phase 10: Collaboration & Sharing</summary> 

🔁 **Inputs:**
- KG Outputs: correlated entities (CVEs, IOCs, TTPs, actor campaigns, asset mappings).  
- Normalized Intel (STIX/TAXII): enriched intel from Phases 1–10, already mapped to standards.  
- Org Policies for Sharing: legal, compliance, and business rules (what can/cannot be shared).  

⚙️ **Inside (Sharing & Collaboration Engine):**  
1. **Intel Selection & Filtering:**  
   - Define sharing policies (e.g., only external-facing IOCs, no internal asset names).  
   - Analysts can manually flag intel for sharing.  
   - Automation rules: “share all malware indicators tied to active APTs.”  

2. **Normalization & Packaging:**  
   - Convert selected KG entities to STIX 2.1 objects (Indicators, Campaigns, Attack Patterns, Relationships).  
   - Bundle intel into STIX packages.  
   - Store in `/data/sharing/stix_packages/`.  

3. **Distribution Mechanisms:**  
   - TAXII Server: serve collections for trusted partners, ISACs, CERTs.  
   - Direct API Push: POST intel to partner ingestion endpoints.  
   - Email/Slack Summaries: high-level sanitized campaign reports for execs/partners.  

4. **Privacy & Anonymization Layer:**  
   - Remove org-specific identifiers (asset names, IPs, employee accounts).  
   - Replace with abstract descriptors (“Finance DB server” → “High-value DB asset”).  
   - Use data minimization rules for compliance (GDPR, CCPA).  

5. **Access Control & Multi-Tenancy:**  
   - Attribute-based access control (ABAC):  
     - Gov CERT partner → receives full adversary TTPs.  
     - Industry ISAC → receives sector-specific intel.  
     - Vendor partner → receives only malware IOCs.  
   - Tiered sharing levels: internal-only, sector-wide, trusted-circle, public.  

6. **Inbound Sharing (Partner → Org):**  
   - Ingest external TAXII/STIX feeds.  
   - Auto-merge into KG with provenance tags (“source=partnerX”).  
   - Detect overlap with local IOCs/campaigns.  
   - Score partner intel quality (timeliness, false-positive ratio).  

7. **Audit & Compliance Logging:**  
   - Every shared item logged in `/logs/sharing_audit.json`.  
   - Track who shared what, when, and with whom.  
   - Generate compliance reports for regulators.  

8. **Collaboration Dashboards:**  
   - `/ui/sharing/overview`: visualize shared intel by partner & campaign.  
   - Graph overlay: internal vs external contributions.  
   - Sharing health metrics: intel volume, reciprocity, overlap ratio.  

📊 **Monitoring & Metrics:**  
- % of intel shared externally vs retained.  
- Partner engagement: # of items received vs contributed.  
- Intel usefulness: how many partner-sourced IOCs were observed in local detections.  
- Sharing latency: time from detection → community distribution.  

🎯 **Purpose:**  
- Promote trusted intelligence exchange without overexposing sensitive data.  
- Strengthen collective defense through ISAC/CERT/partner collaboration.  
- Enable bidirectional flows: not only sharing but also receiving intel into KG.  

📤 **Outputs:**  
- TAXII Collections: hosted at `/taxii/collections/{org_id}/`.  
- Shared STIX Packages: `/data/sharing/stix_packages/*.json`.  
- Partner KG Subsets: partial KG exports tailored to each partner.  

🔁 **Used again in:**  
- Phase 1: ingested external intel enriches Threat Data Acquisition.  
- Phase 12: partner feedback informs the Feedback & Learning loop.  

</details>




<details> <summary>✅ Phase 11: Monitoring, Evaluation & Maintenance</summary> 

🔁 **Inputs:**
- System Logs: ingestion pipeline logs, SOAR/SIEM integrations, chatbot interaction history.  
- User Feedback: analyst corrections, chatbot thumbs-up/down, sharing partner comments.  
- Performance Metrics: response latency, throughput, detection accuracy, coverage ratios.  
- Drift Indicators: schema changes (e.g., new CVE fields), model accuracy decay, new adversary tactics unseen in training.  

⚙️ **Inside (Monitoring & Continuous Improvement):**  
1. **System Performance Monitoring:**  
   - Collect metrics on KG queries (latency, error rate, success/failure ratio).  
   - Track ingestion freshness (lag between CVE release → system ingestion).  
   - Alert if pipelines stall or exceed latency thresholds.  

2. **Model & Data Drift Detection:**  
   - **Data drift:**  
     - Detect changes in external sources (e.g., NVD API updates, new ATT&CK schema).  
     - Schema validation tests on ingestion pipelines.  
   - **Model drift:**  
     - Monitor drop in NLP chatbot accuracy (precision/recall on user queries).  
     - Track CTI entity extraction (NER) degradation against validation sets.  

3. **Evaluation & Benchmarking:**  
   - Maintain golden test sets (known CVEs, sample adversary campaigns, simulated queries).  
   - Run automated regression tests after every pipeline/model update.  
   - Score chatbot answers for factual correctness, coverage, and hallucination rate.  

4. **User Feedback Loop:**  
   - Collect analyst feedback from:  
     - KG corrections (e.g., analyst relabels an IOC).  
     - Chatbot thumbs-up/down.  
     - Partner intel validation (e.g., “false positive IOC”).  
   - Store feedback in `/data/feedback/annotations.json`.  
   - Route feedback to retraining pipelines (Phases 4 & 10).  

5. **Retraining & Maintenance:**  
   - Periodic retraining of ML/LLM models using feedback & drift indicators.  
   - Automate retraining schedules (monthly, or triggered by drift alerts).  
   - Maintain versioned models with rollback capability.  

6. **Compliance & Security Audits:**  
   - Run access audits: track who accessed what KG nodes, who shared intel externally.  
   - Maintain compliance logs for GDPR/CCPA/ISO27001.  
   - Detect policy violations (e.g., restricted data shared externally).  

7. **Bias & Explainability Checks:**  
   - Evaluate ML/LLM outputs for bias (e.g., chatbot prioritizing Western intel sources).  
   - Provide explainability artifacts:  
     - KG reasoning paths for decisions.  
     - Feature importance scores for risk scoring.  
   - Store explainability reports in `/reports/explainability/`.  

8. **Visualization & Dashboards:**  
   - Grafana dashboards for infra health (CPU/mem, pipeline throughput).  
   - Drift dashboards showing model accuracy trends.  
   - Compliance dashboards with sharing logs, access audits, bias findings.  

📊 **Monitoring & Metrics:**  
- KG query latency (avg, p95).  
- Chatbot accuracy (based on validation + user scoring).  
- % ingestion completeness (missed CVEs vs NVD baseline).  
- Drift scores (KL divergence for data, F1 drop for models).  
- Feedback adoption rate (how much analyst feedback was incorporated).  

🎯 **Purpose:**  
- Guarantee long-term reliability of the CTI-KG platform.  
- Ensure trustworthiness and compliance (auditable, explainable outputs).  
- Enable continuous learning from users, partners, and adversary evolution.  

📤 **Outputs:**  
- Grafana Dashboards: `/ui/monitoring/`.  
- Retraining Datasets: `/data/retraining/*.csv`.  
- Compliance & Audit Logs: `/logs/audit/`.  
- Explainability Reports: `/reports/explainability/*.json`.  

🔁 **Used again in:**  
- All phases (feedback loop):  
  - Improves ingestion (Phase 1) via schema validation.  
  - Enhances NLP/Chatbot (Phase 10).  
  - Optimizes attribution accuracy (Phase 5).  
  - Ensures safe sharing (Phase 11).  

</details>






## 📊 Data Pipeline
Details of data ingestion, normalization, enrichment, transformation, storage, and indexing for structured and unstructured threat intelligence sources.

## 🤖 NLP Chatbot
Description of the natural language interface for analysts to query CTI-KG, with examples of questions, intents, responses, and RAG-based enrichment.

## 📈 Visualization & Dashboards
Details of interactive dashboards, attack path visualizations, timeline views, and reporting interfaces for analysts and executives.

## 🔌 API Endpoints
List and description of REST/GraphQL endpoints to access the KG, alerts, dashboards, and other services programmatically.

## 🔗 Integrations
Information on connecting with SIEMs, SOARs, TIPs, ticketing systems, and third-party threat intelligence feeds.

## 💡 Usage Examples
Sample queries, scripts, workflows, and automation examples to demonstrate practical applications of CTI-KG in SOCs and security operations.

## 📊 Monitoring, Feedback & Logging
How the system tracks pipeline performance, captures analyst feedback, maintains audit logs, and provides metrics for continuous improvement.

## 🔒 Security & Compliance
Guidelines for secure data handling, access control, role-based permissions, compliance with GDPR, CCPA, ISO27001, and internal policies.

## 🤝 Contributing
Instructions for external developers to contribute code, report issues, propose features, or improve documentation.

## 📜 License
Legal terms under which the project is released, including the open-source license used (e.g., Apache 2.0).

## 🎉 Acknowledgments
Credits to individuals, organizations, research papers, and open-source projects that contributed to CTI-KG.

## 📚 References / Resources
List of documents, standards, APIs, libraries, tutorials, and external links referenced throughout the project.
