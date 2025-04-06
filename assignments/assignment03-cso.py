import requests
import json

# CSO API URL for the dataset
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
response = requests.get(url)
out = response.json()

with open('cso.json', 'w') as json_file:
    json.dump(out, json_file)