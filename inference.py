from flask import Flask, request, jsonify  
import joblib  
import numpy as np 
import os

# Inicializa a aplicação Flask
app = Flask(__name__)

# Carrega o modelo treinado salvo no arquivo "linear_model.pkl"
model = joblib.load("linear_model.pkl")

# Define o endpoint "/predict" que aceita requisições POST
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Obtém os dados enviados na requisição em formato JSON
        data = request.get_json()

        # Converte os dados recebidos em um array NumPy e os formata como matriz coluna
        X_new = np.array(data["X"]).reshape(-1, 1)

        # Faz a previsão com o modelo carregado e converte o resultado para lista
        prediction = model.predict(X_new).tolist()

        # Retorna a predição em formato JSON
        return jsonify({"prediction": prediction})
    
    except Exception as e:
        # Retorna um erro caso ocorra algum problema no processamento da requisição
        return jsonify({"error": str(e)})

# Inicia o servidor Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Pega a porta do ambiente no Heroku
    app.run(host="0.0.0.0", port=port)
