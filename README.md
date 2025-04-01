# 📊 API de Regressão Linear com Flask, Docker e Heroku

Este projeto implementa uma **API Flask** para fazer previsões usando um modelo de **regressão linear**.  
A API recebe dados via requisições HTTP **POST**, processa as entradas e retorna a predição do modelo treinado.
A aplicação é armazenada e hosteada com auxílio do site Heroku para que se possa fazer requisições de qualquer computador com acesso a internet.

---

## 🚀 **Repositórios**
- **GitHub:** [arthur-ym/heroku](https://github.com/arthur-ym/regressao-linear)  

---

## 📂 **Estrutura do Projeto**
📁 `regressao-linear/`  
├── 📄 `inference.py` → Código principal da API Flask, faz a inferencia do modelo  
├── 📄 `model.py` → Script para treinar e salvar o modelo, modelo simples para simplificar a requisição.

├── 📄 `test_api.py` → Script para testar a API fazendo requisições HTTP, é necessário que o app esteja online para aceitar a requisição.

├── 📄 `requirements.txt` → Lista de bibliotecas necessárias para rodar o projeto.  
├── 📄 `Dockerfile` → Configuração para construir a imagem Docker da API.  
└── 📄 `README.md` → Documentação do projeto.  
└── 📄 `Procfile` → O Procfile define os comandos para iniciar o app na plataforma Heroku

web: gunicorn app:app
Significa:
"Usamos o Gunicorn para rodar a aplicação Flask (app) do arquivo app.py como um servidor web."

Para hostear o app na plataforma é necessário rodar:
heroku container:login
docker build -t registry.heroku.com/test-aym-dev/web .
docker push registry.heroku.com/test-aym-dev/web
heroku container:release web --app test-aym-dev

com "test-aym-dev" sendo o nome do app criado, para reproduzir, basta mudar para um nome de seu app.
No momento minha aplicação esta offline para nao gerar custos.