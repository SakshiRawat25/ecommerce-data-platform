import pandas as pd
import json
import os

path="data/source/orders/2019-Oct.csv"

df = pd.read_csv(path, nrows=10000)
data=df.to_dict(orient="records")

output_folder="data/source/orders"
os.makedirs(output_folder,exist_ok=True)

with open(f"{output_folder}/orders.json", "w") as f:
    json.dump(data,f,indent=4)

print("order data succesfully ingested in bronze")
