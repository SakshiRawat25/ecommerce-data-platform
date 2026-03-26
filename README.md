# 🛒 E-commerce Data Platform (End-to-End)

## ❓ What does it take to build a real-world data pipeline from scratch?

This project simulates a production-grade **E-commerce Data Engineering Platform**, starting from raw data ingestion to building a scalable data lake architecture.

Instead of using static datasets, this project focuses on **real-time external data sources (APIs & files)** to mimic real-world challenges faced by data engineers.

---

## 🚀 Project Objective

To design and implement a complete data pipeline that:

* Ingests data from multiple external sources (APIs, CSV, JSON)
* Stores raw data in a structured data lake format
* Prepares data for downstream processing (PySpark, analytics)
* Follows industry-level folder structure and best practices

---

## 🧩 Architecture

```
APIs / Files
   ↓
Python Ingestion Scripts
   ↓
Airflow (Orchestration - upcoming)
   ↓
Data Lake (Raw Layer)
   ↓
PySpark (Transformation - upcoming)
   ↓
Processed Data (Parquet/Delta)
```

---

## 🛠️ Tech Stack

* **Python** → Data ingestion
* **Git & GitHub** → Version control
* **APIs** → RandomUser, FakeStore, DummyJSON
* **File Formats** → JSON, CSV, XLSX
* **Airflow** (Planned) → Workflow orchestration
* **PySpark** (Planned) → Data transformation
* **MinIO / Data Lake** (Planned) → Storage layer

---

## 📁 Project Structure

```
ecommerce-data-platform/
├── dags/                  # Airflow DAGs
├── ingestion/             # Data ingestion scripts
│   ├── api/
│   ├── files/
├── configs/               # Config files
├── utils/                 # Helper functions
├── data/
│   ├── raw/               # Raw data (ingested)
│   ├── processed/         # Cleaned data
├── logs/                  # Pipeline logs
├── notebooks/             # Exploration
├── tests/                 # Unit tests
├── requirements.txt
└── README.md
```

---

## 🔄 Current Progress

* ✅ Project structure setup
* ✅ GitHub repository setup
* ✅ API-based ingestion (Customers - RandomUser)
* 🔄 More ingestion sources in progress
* ⏳ Airflow integration (coming next)
* ⏳ PySpark transformations

---

## 📥 First Pipeline: Customer Data Ingestion

* Source: RandomUser API
* Format: JSON
* Type: Batch ingestion
* Output: Stored in `data/raw/customers/`

---

## ⚠️ Challenges Faced & How They Were Solved

### 1️⃣ GitHub Permission Error (403)

**Issue:**

```
Permission denied to push repository
```

**Cause:**
Multiple GitHub accounts configured on the system.

**Solution:**

* Cleared stored credentials using Git Credential Manager
* Re-authenticated using browser login
* Used correct GitHub account

---

### 2️⃣ Terminal Freeze During `git push`

**Issue:**
Terminal became unresponsive and did not accept input.

**Cause:**
Git was waiting for hidden credential input (username/password).

**Solution:**

* Cancelled process using `Ctrl + C`
* Enabled credential helper:

  ```
  git config --global credential.helper manager
  ```
* Completed authentication via browser popup

---

### 3️⃣ Empty Folders Not Visible on GitHub

**Issue:**
Project structure appeared incomplete on GitHub.

**Cause:**
Git does not track empty folders.

**Solution:**

* Added `.gitkeep` files inside empty directories
* Committed and pushed changes

---

### 4️⃣ Incorrect Remote URL

**Issue:**
Push failed due to incorrect repository URL.

**Cause:**
Typo in remote URL (`.giter` instead of `.git`)

**Solution:**

```
git remote remove origin
git remote add origin correct-url
```

---

## 📌 Key Learnings

* Git tracks files, not folders
* Credential management is crucial in Git workflows
* Real-world pipelines require handling multiple data sources
* Structuring projects properly from day one is critical

---

## 🚀 Future Enhancements

* Add multiple ingestion pipelines (Products, Orders, Payments)
* Integrate Apache Airflow for scheduling
* Implement PySpark transformations
* Store data in Parquet/Delta format
* Add logging and monitoring
* Deploy using Docker

---

## ⭐ Why This Project Stands Out

* Uses **real external data sources**
* Follows **industry-level architecture**
* Covers **end-to-end data engineering workflow**
* Demonstrates **problem-solving with real issues**

---

## 👩‍💻 Author

**Sakshi Rawat**

---

## 📢 Final Note

This project is being built step-by-step with a focus on **learning, scalability, and real-world relevance**.
