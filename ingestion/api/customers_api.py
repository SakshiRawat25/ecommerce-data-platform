import requests
import json
import os
from datetime import datetime

URL="https://randomuser.me/api/?results=50"

def fetch_customer_data():
    response=requests.get(URL) #Sends a GET request to API
    response.raise_for_status() #If API fails (404, 500 etc.) It throws an error.Without this, your pipeline may silently fail
    return response.json() #Converts API response → Python dictionary

def save_data(data): #This function stores the data in your data lake (local simulation)
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S") # using this to make sure we tracking ingestion time and avoiding overwriting files
    path=f"data/raw/customer/customer_{timestamp}.json"
    # now we have path but what if a folder is missing or so
    os.makedirs(os.path.dirname(path), exist_ok=True)
    #creates folder automatically
    #exist_ok=True → no error if already exists
    with open(path, "w") as f:
        # using with This is called a context manager
        # Why we use it?
        # Automatically closes the file after use
        # Prevents memory leaks
        # Safer than manual open/close
        json.dump(data,f,indent=4)  #Converts Python object → JSON format
        print(f"saved:,{path}")

if __name__ == "__main__":
    data=fetch_customer_data()
    save_data(data)
  









