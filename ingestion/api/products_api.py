import requests
import json
import os
from datetime import datetime

URL='https://fakestoreapi.com/products'

def fetch_product_data():
    response=requests.get(URL)
    response.raise_for_status()
    return response.json()

def save_data(data):
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    path=f"data/raw/product/product_{timestamp}.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data,f,indent=4)
        print(f"Saved:,{path}")

if __name__ == "__main__":
    data=fetch_product_data()
    save_data(data)


    