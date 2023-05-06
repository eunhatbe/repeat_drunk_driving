
import matplotlib.pyplot as plt
import numpy as np

import re
import requests
import pprint
import json

#4fd5b14c-8468-4cb0-93b8-9b182b1553b9
#c90a6f59-d023-426f-9cda-fc2cdbdef96e
#7e08abca-e3db-450d-b2b7-c2dcd2003c3e
uuid_pattern = re.compile(r"([a-f\d]{8})([a-f\d]{4})([a-f\d]{4})([a-f\d]{4})([a-f\d]{12})")

# Key File URL
file_url = "/Users/user/PycharmProjects/repeat_drunk_driving/serviceKey.txt"

# decoding Key
service_key = open(file_url, 'r').readline()

# Swagger URL
swagger_url = "https://infuser.odcloud.kr/oas/docs?namespace=15099959/v1"

headers = {
    'accept': 'application/json',
    'Authorization': service_key,
}

params = {
    'page': '1',
    'perPage': '20',
    'serviceKey': service_key,
}

response = requests.get(
    'https://api.odcloud.kr/api/15099959/v1/uddi:4fd5b14c-8468-4cb0-93b8-9b182b1553b9/',
    params=params,
    headers=headers,
)

if __name__ == "__main__":
    #pprint.pprint(response.json())
    # pprint.pprint(requests.get("https://api.odcloud.kr/api/15099959/v1/uddi:4fd5b14c-8468-4cb0-93b8-9b182b1553b9?page=1&perPage=20&serviceKey=RgUQcuLZUXq5vPZffYY5065M6ioM4%2FbLIJ%2FchDQJspKPMr9Ys4FBVIVnjXd3%2BhOF6mgmQFboWsio4OZeZkXHJQ%3D%3D").json())
    #pprint.pprint(requests.get(swagger_url).json())

    test_data = requests.get(swagger_url).json()
    url = "https://api.example.com/uddi:4fd5b14c-8468-4cb0-93b8-9b182b1553b9/data"
    match = re.search(r'uddi:(\w+)', url)

    

    
