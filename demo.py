from datetime import datetime

import pandas as pd
import requests


# HKIA historical flight API
API_URL = ("https://www.hongkongairport.com/flightinfo-rest/rest/flights/past")


# Current demonstration settings
TARGET_DATE = "2026-07-19"
LANGUAGE = "en"
REQUEST_TIMEOUT = 30


# Departure passenger flight parameters
ARRIVAL = "false"
CARGO = "false"


# Current PoC gate configuration
ROBOT_GATES = {
    "511",
    "512",
    "513",
    "514",
    "515",
    "520",
    "521",
    "522",
    "523",
    "524",
}

# 在這裏加入 fetch_flight_data()

def fetch_flight_data():
    params = {
        "date": TARGET_DATE,
        "arrival": ARRIVAL,
        "cargo": CARGO,
        "lang": LANGUAGE,
    }

    print("\nSending request to HKIA API...")

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")
        return None
    
    except requests.exceptions.HTTPError as error:
        print("Error: The API returned an HTTP error.")
        print("Details:", error)
        return None
    
    except requests.exceptions.JSONDecodeError:
        print("Error: The API response is not valid JSON.")
        return None 
    
    except requests.exceptions.RequestException as error:
        print("Error: The API request failed.")
        print("Details:", error)
        return None
    
    print("Request completed successfully.")
    print("Status code:", response.status_code)
    print("Final URL:", response.url)
    print(
        "Content type:", response.headers.get("Content-Type"),
    )
    
    return data

def main():
    fetched_at = datetime.now()

    print("=" * 50)
    print("HKIA Flight Data Demo")
    print("=" * 50)

    print("Data source: HKIA historical flight API")
    print("Flight scope: Departure passenger")
    print("Target date:", TARGET_DATE)
    print("Language:", LANGUAGE)
    print("Request timeout:", REQUEST_TIMEOUT, "seconds")
    print("Configured robot gates:", sorted(ROBOT_GATES))
    print(
        "Program started at:",
        fetched_at.strftime("%Y-%m-%d %H:%M:%S")
    )
     
    data = fetch_flight_data()

    if data is None:
        print(
            "\nThe program stopped because data could not be retrieved."
        )
        return

    if not isinstance(data, list):
        print("\nError: Expected the API response to be a list.")
        print("Actual data type:", type(data))
        return
    
    print("\nAPI data summary:")
    print("Outer data type:", type(data))
    print("Number of outer items:", len(data))

if __name__ == "__main__":
    main()


