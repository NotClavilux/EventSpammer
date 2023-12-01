import requests
import time
import json

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

url = config["url"]
payload = config["payload"]
headers = config["headers"]

while True:
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)

    time.sleep(5)
