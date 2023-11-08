import requests
from pprint import pprint

url = "https://api.datadoghq.com/api/v1/dashboard/"+ '35t-e4b-4t2'

headers = {
    "Accept": "application/json",
    "DD-API-KEY": "d0a19e336b72a5db66388aaf69cf7142",
    "DD-APPLICATION-KEY": "ca5fdfc7ef2db9242ed3e0e0ea2f9918e65f6fce"
}

response = requests.get(url, headers=headers)

pprint(response.json())
