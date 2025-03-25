import requests
import csv
import os

def get_all_ev_charging_stations_with_address(country_code="US", api_key="api_key", batch_size=1000):
    
    url = "https://api.openchargemap.io/v3/poi"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    offset = 0
    all_addresses = []
    
    while True:
        params = {
            "key": api_key,
            "output": "json",
            "countrycode": country_code,
            "compact": True,
            "verbose": False,
            "maxresults": batch_size,
            "offset": offset
        }
        
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print("Response text:", response.text)
            break
        
        data = response.json()
        if not data:
            print("No more data to download.")
            break
        
        for station in data:
            address_info = station.get("AddressInfo", {})
            address = {
                "Title": address_info.get("Title", "N/A"),
                "AddressLine1": address_info.get("AddressLine1", "N/A"),
                "Town": address_info.get("Town", "N/A"),
                "StateOrProvince": address_info.get("StateOrProvince", "N/A"),
                "Postcode": address_info.get("Postcode", "N/A"),
                "Country": address_info.get("Country", {}).get("Title", "N/A")
            }
            all_addresses.append(address)
        
        offset += len(data)
        print(f"Downloaded {offset} records...")
        
        if len(data) < batch_size:
            break

    return all_addresses

def write_to_csv(data, filename):
    if not data:
        print("No data to write.")
        return
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.exists(desktop_path):
        one_drive_desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
        if os.path.exists(one_drive_desktop):
            desktop_path = one_drive_desktop

    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path, exist_ok=True)
    
    file_path = os.path.join(desktop_path, filename)
    keys = data[0].keys()  
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data written to {file_path}")

if __name__ == "__main__":
  
    addresses = get_all_ev_charging_stations_with_address(country_code="US", api_key="b36eb2ab-fcc3-4621-b091-efbaed478e5c", batch_size=1000)
    write_to_csv(addresses, "all_ev_charging_stations_USA.csv")
