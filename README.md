Project Overview
This project is a data integration and analysis pipeline for MCA company datasets from multiple Indian states. It ingests raw CSV files, cleans and normalizes data, enriches change logs, and provides an interactive Streamlit dashboard for search and exploration.

Submitted Files

app_mca.py
Python script containing the full data pipeline.
Reads multiple state-wise CSV files.
Cleans and normalizes columns and data types.
Enriches data with change logs (with safe fallback).
Provides an optional Streamlit UI for interactive data exploration with search and pagination.
Includes code comments for clarity.
MCA_Insights_Engine_Assignment_Final.pdf
Detailed project documentation.


Explains problem statement, data sources, methodology, and results.

Contains screenshots and usage instructions.

Summarizes key learnings and next steps.

Running the Code
Prerequisites
Python 3.8 or later

Packages: pandas, streamlit

Installation (example commands)
bash
pip install pandas streamlit
Running the Streamlit App
bash
streamlit run app_mca.py
This launches an interactive web app.

Use the search box to filter companies by CIN or company name.

The dataset display is paginated for performance.

Notes
Update CSV file paths in app_mca.py as per your local environment.

The app auto-creates sample change log data if the real file is not found.

The solution handles large datasets and common errors gracefully.
