#Questao 01:
#import requests

#url = "https://viacep.com.br/ws/53520155/json/"
#resposta = requests.get(url, timeout=10)

#print(resposta.json())

#Questao 02:
#import requests

#url = "https://viacep.com.br/ws/00000000/json/"
#resposta = requests.get(url, timeout=10)

#print("Status:", resposta.status_code)
#print(resposta.json())

#Questao 03:
#import requests

#url = "https://viacep.com.br/ws/abc/json/"
#resposta = requests.get(url, timeout=10)

#print("Status:", resposta.status_code)
#print("texto da resposta:", resposta.text)

#import requests

#url = "https://viacep.com.br/ws/53520155/json/"
#resposta = requests.get(url, timeout=10)

#print("Status:", resposta.status_code)
#print("texto da resposta:", resposta.json())

import requests


def consultar_cep(cep: str) -> dict | None:
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

    except requests.exceptions.Timeout:
        print(f"[erro] ViaCEP demorou demais (CEP={cep})")
        return None

    except requests.exceptions.ConnectionError:
        print("[erro] Sem conexão ou servidor fora do ar")
        return None

    except requests.exceptions.HTTPError as erro:
        print(f"[erro] HTTP {resposta.status_code}: {erro}")
        return None

    dados = resposta.json()

    # O ViaCEP retorna HTTP 200 mesmo quando o CEP não existe.
    if dados.get("erro"):
        print(f"[aviso] CEP {cep} não existe")
        return None

    return dados


if __name__ == "__main__":
    for cep in ["52050480", "00000000", "01310100"]:
        endereco = consultar_cep(cep)

        if endereco:
            print(cep, endereco["logradouro"], endereco["bairro"])