import requests

url = "https://api.openweathermap.org/data/2.5/weather"
resposta = requests.get(url, params={"q": "Recife,BR"}, timeout=10)
print("Status:", resposta.status_code)
print(resposta.text)