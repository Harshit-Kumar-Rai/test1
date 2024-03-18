import requests

url = "http://13.126.132.164:8000/api/user/ajeevi/1234"
response = requests.get(url)
print('Status code:', response.status_code)
print(response.json())
print(response.headers)