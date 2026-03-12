# Healthcare Data Platform (Databricks)

End-to-end **Healthcare Quality Assurance (QA) Data Engineering Platform** built using **Databricks**, implementing the **Medallion Architecture (Bronze → Silver → Gold)** to process, clean, and analyze laboratory QA datasets.

This project simulates a **real-world healthcare/pharmaceutical data pipeline** where raw laboratory testing data is ingested, cleaned, and transformed into analytics-ready datasets.

---

# Project Overview

Healthcare and pharmaceutical laboratories generate large volumes of **Quality Assurance (QA) testing data**.
This platform demonstrates how such data can be processed using a modern data engineering architecture.

The pipeline includes:

* Raw data ingestion
* Data quality validation
* Data cleaning and transformation
* Analytical data modeling
* Data quality monitoring

The dataset used in this project contains **20K+ healthcare QA records**, including **intentional dirty data (~6%)** such as:

* Duplicate records
* Null values
* Invalid status values
* Datatype inconsistencies
* Garbage text values

These issues are cleaned during the **Silver layer transformation**.

---

# Architecture

```
                +---------------------+
                |   Source CSV Data   |
                |  (QA Lab Dataset)   |
                +----------+----------+
                           |
                           v
                +---------------------+
                |     Bronze Layer    |
                |  Raw Data Ingestion |
                |  No Transformation  |
                +----------+----------+
                           |
                           v
                +---------------------+
                |     Silver Layer    |
                |   Data Cleaning     |
                |  - Remove duplicates|
                |  - Handle nulls     |
                |  - Fix datatypes    |
                |  - Standardize data |
                +----------+----------+
                           |
                           v
                +---------------------+
                |      Gold Layer     |
                | Analytics & Metrics |
                | QA KPIs / Reporting |
                +----------+----------+
                           |
                           v
                +---------------------+
                |   BI / Dashboard    |
                |   Quality Insights  |
                +---------------------+
```

---

# Tech Stack

| Component       | Technology             |
| --------------- | ---------------------- |
| Data Platform   | Databricks             |
| Storage Format  | Delta Lake             |
| Processing      | Apache Spark           |
| Language        | PySpark / SQL          |
| Version Control | GitHub                 |
| Architecture    | Medallion Architecture |

---

# Dataset Description

The dataset simulates **Healthcare / Pharmaceutical QA testing data**.

### Key Fields

| Column           | Description                          |
| ---------------- | ------------------------------------ |
| label_id         | Unique QA label identifier           |
| sample_number    | Sample tracking number               |
| lot_name         | Manufacturing batch ID               |
| lot_number       | Batch reference number               |
| item_description | Product form (tablet, capsule, etc.) |
| test_number      | Laboratory test ID                   |
| name             | Test name (Assay, Purity, Stability) |
| product          | Product category                     |
| status           | QA test status                       |
| product_grade    | Product quality grade                |
| x_method         | Lab testing method (HPLC, GC, UV)    |
| result_number    | Test result identifier               |

---

# Medallion Architecture

## Bronze Layer (Raw Data)

Purpose:

* Store raw ingested data
* Preserve original dataset
* Enable traceability

Example table:

```
healthcare.bronze.qa_sample_raw
```

Characteristics:

* No transformations
* Raw CSV ingestion
* Schema inferred

---

## Silver Layer (Data Cleaning)

Purpose:

* Clean and standardize the raw dataset

Transformations:

* Remove duplicate records
* Trim whitespace
* Handle null values
* Fix datatype errors
* Normalize text casing
* Validate status fields

Example table:

```
healthcare.silver.qa_sample_clean
```

Example cleaning logic:

```
Remove duplicates
Fix datatype issues
Trim text columns
Standardize product names
```

---

## Gold Layer (Business Analytics)

Purpose:
Provide **analytics-ready datasets** for reporting and dashboards.

Example metrics:

* QA test completion rate
* Product quality distribution
* Tests performed by method
* Batch validation statistics

Example table:

```
healthcare.gold.qa_quality_metrics
```

---

# Repository Structure

```
healthcare-data-platform
│
├── data
│   └── healthcare_lab_data
│       └── healthcare_lab_dataset.csv
├── notebooks
│   ├── 01_bronze_ingestion
│   ├── 02_silver_data_cleaning
│   └── 03_gold_analytics
│
├── docs
│   └── architecture.md
│
└── README.md
```

---

# Example Pipeline Flow

```
CSV Dataset
    ↓
Bronze Table
    ↓
Data Cleaning Transformations
    ↓
Silver Table
    ↓
Aggregation & Metrics
    ↓
Gold Analytics Tables
```

---

# Key Data Engineering Concepts Demonstrated

This project demonstrates several important **real-world data engineering practices**:

* Medallion architecture
* Data quality handling
* Data pipeline design
* Spark-based transformations
* Data governance structure
* Delta table modeling

---

# Future Improvements

Possible extensions:

* Implement Delta Live Tables
* Add data quality monitoring
* Build automated pipelines
* Create BI dashboards
* Implement CI/CD pipelines

