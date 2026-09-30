# My_ETL_Pipeline-

Flipkart Sales ETL Pipeline

A simple, beginner-friendly ETL (Extract, Transform, Load) pipeline built in Python. It reads raw sales/match data from a CSV file, cleans it, and saves a clean version — ready for analysis or loading into a data warehouse like Snowflake.



This project was built as part of my Data Engineering learning journey, to practice core DE concepts: OOP, file handling, data cleaning with Pandas, logging, and error handling.

What It Does
Raw CSV  →  Extract  →  Transform  →  Load  →  Clean CSV
Extract — Reads the raw CSV file using Pandas.
Transform — Cleans the data:
Converts date columns to proper datetime format
Strips extra whitespace from text columns
(Add more cleaning rules here as the project grows)
Load — Saves the cleaned data to a new CSV file, creating the output folder automatically if it doesn't exist.
Tech Used
Tool	Purpose
Python	Core language
Pandas	Data cleaning & transformation
logging	Tracking pipeline progress and errors
pathlib	Safe, cross-platform file path handling
python-dotenv	Keeping file paths/credentials out of the code
Setup Instructions
1. Clone the repo
bash

2. Install dependencies
bash
pip install -r requirements.txt
3. Create your own .env file

Copy .env.example and rename it to .env, then fill in your own local paths:

INPUT_FILE=path/to/your/input.csv
OUTPUT_FILE=path/to/your/output/clean_data.csv

Your .env file is private and will never be uploaded to GitHub (it's listed in .gitignore).

4. Run the pipeline
bash
python pipeline.py

If successful, you'll see logs like:

INFO:root:Reading CSV file...
INFO:root:Transform CSV file...
INFO:root:Saving cleaned data...
INFO:root:Pipeline completed successfully!
What I Learned Building This
Structuring code using OOP (a class with extract, transform, load, and run methods)
Using Pandas to inspect (df.info()) and clean real-world messy data
Handling file paths safely across systems using pathlib
Using logging instead of print() for professional-level tracking
Handling errors gracefully with try-except so the pipeline fails informatively instead of crashing
Keeping sensitive information (file paths/credentials) out of source code using .env files
Future Improvements
 Add more data validation/cleaning rules
 Load cleaned data directly into Snowflake
 Add automated tests
 Schedule the pipeline to run automatically (e.g., with Airflow)
Author

Built by Ravindra Chilhate as part of my Data Engineering learning journey.
