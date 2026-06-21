# BigMart ETL Project

## Overview

This project demonstrates an end-to-end Data Engineering pipeline using PySpark and Medallion Architecture.

The pipeline processes BigMart sales data through Bronze, Silver, and Gold layers.

## Tech Stack

* PySpark
* Databricks
* Delta Lake
* GitHub
* Python

## Project Structure

```text
bigmart_etl/
│
├── src/
│   ├── 01_bronze.py
│   ├── 02_silver.py
│   └── 03_gold.py
│
├── README.md
└── .gitignore
```

## Data Flow

```text
BigMart Sales.csv
        ↓
Bronze Layer
(Raw Data)
        ↓
Silver Layer
(Cleaned & Standardized Data)
        ↓
Gold Layer
(Business Aggregations)
```

## Bronze Layer

* Reads raw CSV data
* Adds ingestion timestamp
* Stores raw data

## Silver Layer

* Cleans and standardizes data
* Handles null values
* Casts columns to appropriate datatypes
* Removes duplicates

## Gold Layer

* Creates business-level aggregations
* Calculates:

  * Total Items
  * Average MRP
  * Total Sales
  * Average Sales

## Learning Objectives

* PySpark DataFrames
* Data Ingestion
* Data Cleaning
* Aggregations
* Medallion Architecture
* Delta Tables
* Databricks Workflows

## Future Enhancements

* Delta Live Tables (DLT)
* Databricks Workflows
* Data Quality Checks
* Incremental Processing
* Unit Testing
* CI/CD Pipeline
