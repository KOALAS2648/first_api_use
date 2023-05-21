import requests # https://randomfox.ca/floof
from selenium import webdriver

response = requests.get("https://randomfox.ca/floof")
# tell us if the request was code using codes: 200 is good
print(response.status_code)
status_code = response.status_code
# gives the json format of the links and images like a dict
fox = response.json()
image = fox["image"]
print(fox["image"])
