# HKIA Flight Data Extraction

A Python project that retrieves historical flight information from the
Hong Kong International Airport API and exports flight records to CSV.

## Current milestone

- Send an HTTP GET request to the HKIA API
- Pass date, arrival, cargo, and language parameters
- Parse and validate the JSON response
- Process multiple outer response items
- Extract departure passenger flight records
- Create a pandas DataFrame
- Export the result to CSV

## Requirements

- Python 3
- requests
- pandas

## Installation

Create and activate a Python virtual environment, then install the
required packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```