
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
uddi_data_list = requests.get(swagger_url).json()


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

def parser_uddi(data: any) -> list:
    operations = []
    temp = []

    for path in data["paths"]:
        for method in data["paths"][path]:
            if "operationId" in data["paths"][path][method]:
                if data["paths"][path][method]["operationId"].startswith("getuddi:"):
                    operations.append(data["paths"][path][method]["operationId"])

    for operation in operations:
        code = operation.split(':')[1]
        temp.append(code)

    operations = temp
    return operations


if __name__ == "__main__":
    #pprint.pprint(response.json())
    # pprint.pprint(requests.get("https://api.odcloud.kr/api/15099959/v1/uddi:4fd5b14c-8468-4cb0-93b8-9b182b1553b9?page=1&perPage=20&serviceKey=RgUQcuLZUXq5vPZffYY5065M6ioM4%2FbLIJ%2FchDQJspKPMr9Ys4FBVIVnjXd3%2BhOF6mgmQFboWsio4OZeZkXHJQ%3D%3D").json())
    #pprint.pprint(requests.get(swagger_url).json())

    uddi_list = parser_uddi(uddi_data_list)
    big_data = []

    for uddi in uddi_list:
        json_data = requests.get(f'https://api.odcloud.kr/api/15099959/v1/uddi:{uddi}',params=params,headers=headers,).json()
        big_data.append(json_data)

    print(big_data)
