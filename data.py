'''
#Testing for enviormente
import sys
import requests
import pandas as pd

print("Python executable:")
print(sys.executable)

print("\nPackage versions:")
print("requests:", requests.__version__)
print("pandas:", pd.__version__)

print("\nSetup completed successffuly.")
'''


import requests
import pandas as pd

# STEP 1: Define HKIA Historical Flight Information API Endpoint
url = "https://www.hongkongairport.com/flightinfo-rest/rest/flights/past"

# STEP 2: Define the query parameters
params = {
    "date": "2026-07-19",
    "arrival": "false",
    "cargo": "false",
    "lang": "en"
}

print("Sending request to HKIA API...")
print("Parameters:", params)

# STEP 3: Send the request and parse the JSON

try:
    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    # Raise an HTTPError for 4xx and 5xx responses
    response.raise_for_status()

    # Convert the JSON response into Python objects
    data = response.json()

    print("\nRequest completed.")
    print("Status code:", response.status_code)
    print("Final URL:", response.url)
    print("Content type:", response.headers.get("Content-Type"))
    
    print("\nJSON parsed successfully.")
    print("Outer data type:", type(data))

    if isinstance(data,  list):
        print("Number of outer items:", len(data))

        if len(data) > 0:
            first_item = data[0]

            print("First item type:", type(first_item))
            print("First item keys:", list(first_item.keys()))



except requests.exceptions.Timeout:
    print("\nError: The API request timed out.")
    raise SystemExit

except requests.exceptions.HTTPError as error:
    print("\nHTTP error:", error)
    raise SystemExit

except requests.exceptions.RequestException as error:
    print("\nRequest failed:", error)
    raise SystemExit

except ValueError:
    print("\nError: The response is not valid JSON.")
    raise SystemExit

# STEP 4: Validate the outer JSON structure

if not isinstance(data, list):
    print("\nError: Expected the outer JSON data to be a list.")
    print("Actual data type:", type(data))
    raise SystemExit

if len(data) == 0:
    print("\nNo outer item were returned by the API.")
    raise SystemExit

# STEP 5: Inspect every outer item

print("\nOuter item summary:")

for index, item in enumerate(data):
    if not isinstance(item, dict):
        print(
            f"\nWarning: Outer item {index} "
            "is not a dictionary and will be skipped."
        )
        continue

    print(f"\nOuter item {index}:")
    print("Date:", item.get("date", ""))
    print("Arrival:", item.get("arrival"))
    print("Cargo", item.get("cargo"))
    print("Last updated time:", item.get("lastUpdatedTime", ""))

    flight_list = item.get("list", [])

    print("Number of flight records:", len(flight_list))

    if len(flight_list) > 0:
        first_flight = flight_list[0]

        print("First flight record keys:", list(first_flight.keys()))

# STEP 6: Extract and flatten all flight records

records = []

for item in data:
    if not isinstance(item, dict):
        continue

    response_date = item.get("date", "")
    flight_list = item.get("list", [])

    if not isinstance(flight_list, list):
        continue

    for flight in flight_list:
        if not isinstance(flight, dict):
            continue
        
        record = {
            "Date": response_date,
            "Time": flight.get("time", ""),
            "Terminal": flight.get("terminal", ""),
            "Gate": flight.get("gate", ""),
            "Status": flight.get("status", "")
        }

        records.append(record)

print("\nExtraction summary:")
print("Number of extracted records:", len(records))

if len(records) > 0:
    print("First extracted record:", records[0])
    print("Last extracted record:", records[-1])

# STEP 7: Create a pandas DataFrame

df = pd.DataFrame(
    records,
    columns=[
        "Date",
        "Time",
        "Terminal",
        "Gate",
        "Status"
    ]
)

print("\nDataFrame preview:")
print(df.head())

print("\nDataFrame information:")
print("Number of rows:", len(df))
print("Number of columns", len(df.columns))
print("Column names:", list(df.columns))

# STEP 8: Validate the DataFrame

if df.empty:
    print("\nNo flight records were extracted.")
    raise SystemExit

print("\nBlank-value summary:")
print("Blank Date:", (df["Date"] == "").sum())
print("Blank Time", (df["Time"] == "").sum())
print("Blank Terminal:", (df["Terminal"] == "").sum())
print("Blank Gate:", (df["Gate"] == "").sum())
print("Blank Status:", (df["Status"] == "").sum())

#STEP 9: Export the DataFrame to CSV

output_file = f"hkia_departure_{params['date']}.csv"

try:
    df.to_csv(
        output_file,
        index = False,
        encoding = "utf-8-sig"
    )

    print("\nCSV created successfully.")
    print("Output file:", output_file)

except PermissionError:
    print(
        "\nError: The CSV file cannot be written. "
        "Please close the file in Excel and try again."
    )
    raise SystemExit

except OSError as error:
    print("\nError: The CSV could not be created.")
    print("Details:", error)
    raise SystemExit











