import requests

# URL do endpoint da API
API_URL = "http://localhost:5000/predict"

# Dados de entrada para teste
data = {"X": [2, 5, 10]}

# Enviando uma requisição POST
response = requests.post(API_URL, json=data)

# Exibindo a resposta da API
if response.status_code == 200:
    print("Resposta da API:", response.json())
else:
    print("Erro:", response.status_code, response.text)
