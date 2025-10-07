# Women in Politics Dashboard 🌍

This project is a **data engineering and visualization project** that tracks women's political representation globally using **World Bank data**. It features a full **ETL pipeline**, a **PostgreSQL database**, and an **interactive Streamlit dashboard**.

---

## Project Overview

The goal of this project is to analyze and visualize trends of women in parliament worldwide. Users can:

- Explore the **percentage of women in parliament** by country over time.
- Compare **global representation** for a selected year with a world map.
- Filter and visualize **specific countries** interactively.

This project demonstrates skills in **data extraction, transformation, loading (ETL), database management, and data visualization** — perfect for showcasing **data engineering expertise**.

---

## Technologies Used

- **Python** – for ETL scripts and dashboard development  
- **Pandas** – data manipulation  
- **SQLAlchemy** – database connection to PostgreSQL  
- **PostgreSQL** – data storage  
- **Streamlit** – interactive dashboard  
- **Plotly Express** – interactive charts  
- **World Bank API** – source of data

---


## Getting Started

### Prerequisites

1. **Python 3.10+** installed  
2. **PostgreSQL 15/18+** installed and running locally  
3. **Required Python packages**:  

```powershell
python -m pip install -r requirements.txt
```

---

## Step 1 — Set up PostgreSQL

Open PostgreSQL and create a new database:
```powershell
CREATE DATABASE women_politics;
```
Update your password in etl/load_data.py:
```powershell
engine = create_engine("postgresql://postgres:<your_password>@localhost:5432/women_politics")
```
## Step 2 — Run the ETL pipeline

From the main folder, run:
```powershell
python run_pipeline.py
```
This will:

Extract data from the World Bank API

Transform it to a clean format

Load it into your PostgreSQL database

## Step 3 — Run the Streamlit dashboard
```powershell
python -m streamlit run dashboard.py
```
A browser window will open at http://localhost:8501.

You can interactively:

Select a country to see trends over time

Use the slider to see global representation for a specific year

Explore data with interactive charts

--

## Data Source

Data comes from the World Bank’s Women in Parliament dataset:

World Bank API