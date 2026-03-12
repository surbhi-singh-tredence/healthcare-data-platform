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