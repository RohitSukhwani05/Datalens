# DataLens — CSV Data Quality Dashboard

DataLens is a beginner-friendly Python web app that helps users explore CSV files, identify data quality issues, clean data, and visualize numerical values.

## Features

* Upload CSV files.
* Preview uploaded data.
* View the number of rows and columns.
* Detect missing values in each column.
* Detect duplicate rows.
* Optionally remove rows with missing values.
* Optionally remove duplicate rows.
* Preview cleaned data and download it as a CSV file.
* Visualize numerical columns with charts.

## Technologies Used

* Python
* Pandas
* Streamlit
* Plotly

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/RohitSukhwani05/DataLens.git
cd datalens
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create and activate a virtual environment

On Windows:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```cmd
python -m pip install pandas streamlit plotly pytest
```

### 4. Run the application

```cmd
python -m streamlit run app.py
```

The app will open in your browser.

## Project Status

This is a learning project that is being developed incrementally. More improvements and tests may be added over time.
