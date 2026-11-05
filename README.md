# HKIA Flight Data Extraction

A learning-oriented Python project that retrieves publicly available historical flight information from the Hong Kong International Airport API, validates the JSON response, processes selected departure flight records, and exports the results to CSV.

## Project Purpose

This project was developed as a learning exercise to practise API-based data extraction, JSON parsing, structured data validation, and data transformation using Python and pandas.

## Features

- Send an HTTP GET request to the HKIA API
- Pass date, arrival, cargo, and language parameters
- Parse and validate nested JSON responses
- Process multiple outer response items
- Extract selected departure passenger flight records
- Transform the extracted records into a pandas DataFrame
- Perform basic data-quality checks
- Export the processed results to CSV

## Technologies Used

- Python 3
- pandas
- requests
- REST API
- JSON
- Git and GitHub

## Project Structure

- `data.py`: Retrieves, validates, and processes historical flight data
- `demo.py`: Demonstrates an API request and data-processing workflow
- `requirements.txt`: Lists the required Python packages
- `.gitignore`: Excludes generated and unnecessary files

## Installation

Clone the repository:

```bash
git clone https://github.com/paulpyy/hkia-flight-data-extraction.git
cd hkia-flight-data-extraction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the demonstration script:

```bash
python demo.py
```

The script retrieves historical departure flight information, processes the selected records, and creates a CSV output file.

## Skills Demonstrated

- Python programming
- REST API integration
- JSON parsing and validation
- Data cleaning and transformation
- pandas DataFrame construction
- CSV export
- Basic exception handling
- Git version control

## Limitations

This is a learning-oriented project and is not intended to be a production system. API availability, parameters, and response formats may change over time.

The project focuses on data extraction and validation. It does not contain financial forecasting, investment models, or trading strategies.

## Data and Confidentiality

This repository contains code developed for learning purposes and uses information available through public sources. It does not contain confidential, proprietary, or internal operational data.
