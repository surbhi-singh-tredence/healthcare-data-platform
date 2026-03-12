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
                |    Facts & Dims     |
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
├── ddl
│   └── healthcare_lab_gold_schema.sql
│
├── docs
│   └── architecture.md
│
├── env
│   └── _environment_setup
│
├── notebooks
│   ├── 01_bronze_ingestion
│   ├── 02_silver_data_cleaning
│   └── 03_gold_star_schema_load
│
├── src
│   ├── ingestion
│   │   └── bronze_loader.py
│   │
│   └── transformations
│       └── silver_cleaning.py
│
├── utils
│   └── logger.py
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
Gold Analytics Tables (Fact & Dims)
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

* Add data quality monitoring
* Build automated pipelines
* Create BI dashboards
* Implement CI/CD pipelines