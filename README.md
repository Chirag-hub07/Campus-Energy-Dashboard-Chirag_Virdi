Campus Energy Dashboard – Capstone Project
-------------------------------------------
📌 Project Overview
--------------------
This project analyzes electricity consumption across multiple campus buildings using Python. It reads raw meter data, cleans and merges files, generates daily and weekly usage summaries, builds an object-oriented model for buildings, and creates a multi-chart energy dashboard.

📂 Features
------------
Automatic ingestion of multiple CSV files

Exception handling for missing or corrupted datasets

Daily and weekly consumption analysis

Building-wise summary (mean, min, max, total)

OOP modeling using Building, MeterReading, and BuildingManager

Dashboard containing line, bar, and scatter plots

Exports cleaned data, summary CSV, and a text report

📁 Project Structure
---------------------
campus-energy-dashboard/
│ capstone.py
│ README.md
│ dashboard.png
│ cleaned_energy_data.csv
│ building_summary.csv
│ summary.txt
│
└── data/
    ├── engineering_block.csv
    ├── library.csv
    ├── admin_block.csv
    └── hostel_block.csv

📊 Visualizations Included
---------------------------
Trend Line: Daily energy consumption

Bar Chart: Weekly average usage for each building

Scatter Plot: Peak-hour consumption distribution

All plots are combined into dashboard.png.

📌 How to Run
--------------
Place all CSV datasets inside the data/ folder.

Run the script:

python dashboard.py


Output files will be generated automatically:

cleaned_energy_data.csv

building_summary.csv

summary.txt

dashboard.png

📜 Summary Report Includes
---------------------------
Total campus energy usage

Highest-consuming building

Peak load timestamp

Observed usage trends

📘 Learning Outcomes
---------------------
Working with real-world datasets

Data cleaning and preprocessing

Aggregation using Pandas

Object-oriented programming

Multi-chart visualization in Matplotlib

Automated reporting and file export
