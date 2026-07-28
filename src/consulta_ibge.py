import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
resposta = requests.get(url, timeout=10)

print("Status:", resposta.status_code)

estados = resposta.json()

print("Tipo:", type(estados))
print("Quantos estados?", len(estados))
print(estados[0])

print("\nEstados do Nordeste:")

for estado in estados:
    if estado["regiao"]["sigla"] == "NE":
        print(f' {estado["sigla"]} - {estado["nome"]}')