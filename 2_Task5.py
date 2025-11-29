import requests

response = requests.get(f"https://randomuser.me/api/")
print(response.json())
