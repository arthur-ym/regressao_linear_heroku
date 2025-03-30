# 📊 API de Regressão Linear com Flask e Docker

Este projeto implementa uma **API Flask** para fazer previsões usando um modelo de **regressão linear**.  
A API recebe dados via requisições HTTP **POST**, processa as entradas e retorna a predição do modelo treinado.

---

## 🚀 **Repositórios**
- **GitHub:** [arthur-ym/regressao-linear](https://github.com/arthur-ym/regressao-linear)  
- **Docker Hub:** [arthurym25/regressaolinear](https://hub.docker.com/repository/docker/arthurym25/regressaolinear/general)

---

## 📂 **Estrutura do Projeto**
📁 `regressao-linear/`  
├── 📄 `app.py` → Código principal da API Flask.  
├── 📄 `model.py` → Script para treinar e salvar o modelo de regressão linear.  
├── 📄 `test_api.py` → Script para testar a API fazendo requisições HTTP.  
├── 📄 `requirements.txt` → Lista de bibliotecas necessárias para rodar o projeto.  
├── 📄 `Dockerfile` → Configuração para construir a imagem Docker da API.  
└── 📄 `README.md` → Documentação do projeto.  

---

## 🏗 **Instalação e Execução**

### 🔹 **1. Clonar o Repositório**
```bash
git clone https://github.com/arthur-ym/regressao-linear.git
cd regressao-linear
