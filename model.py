# model.py

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Gerando dados para a regressão
# Pegamos um modelo linear simples com ruído para simplificar o exemplo
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Variável independente
y = 3 * X + np.random.randn(100, 1) * 2  # Variável dependente

# Criando e treinando o modelo
model = LinearRegression()
model.fit(X, y)

# Salvando o modelo treinado
joblib.dump(model, "linear_model.pkl")

print(f"Coeficiente: {model.coef_[0][0]:.2f}")
print(f"Intercepto: {model.intercept_[0]:.2f}")
