
import matplotlib.pyplot as plt
import numpy as np

import requests
import pprint
import json

# Key File URL
file_url = "/Users/user/PycharmProjects/repeat_drunk_driving/serviceKey.txt"

# decoding Key
service_key = open(file_url, 'r').readline()

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
    'https://api.odcloud.kr/api/15099959/v1/uddi:4fd5b14c-8468-4cb0-93b8-9b182b1553b9',
    params=params,
    headers=headers,
)

if __name__ == "__main__":
    pprint.pprint(response.json())
