import urllib.request
import os

variables = {
    "Tmax": "Tmax",
    "Tmin": "Tmin", 
    "Tmean": "Tmean",
    "Sunshine": "Sunshine",
    "Rainfall": "Rainfall",
    "Raindays1mm": "Raindays1mm",
    "AirFrost": "AirFrost",
}

regions = [
    "UK", "England", "Wales", "Scotland", "Northern_Ireland",
    "England_and_Wales", "England_N", "England_S",
    "Scotland_N", "Scotland_E", "Scotland_W",
    "England_E_and_NE", "England_NW_and_N_Wales",
    "Midlands", "East_Anglia",
    "England_SW_and_S_Wales", "England_SE_and_Central_S",
]

base_url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets"
os.makedirs("metoffice_data", exist_ok=True)

for var in variables:
    for region in regions:
        url = f"{base_url}/{var}/date/{region}.txt"
        dest = f"metoffice_data/{var}_{region}.txt"
        try:
            urllib.request.urlretrieve(url, dest)
            print(f"OK: {var}/{region}")
        except Exception as e:
            print(f"SKIP: {var}/{region} ({e})")
