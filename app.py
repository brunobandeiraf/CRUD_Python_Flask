from flask import Flask  # Importa a classe Flask do módulo flask

app = Flask(__name__)  # Cria uma instância da aplicação Flask

@app.route("/")  # Define a rota para a URL raiz ("/")
def hello_world():
    return "Hello world!"  # Retorna uma resposta simples para a rota raiz

@app.route("/about")  # Define a rota para a URL "/about"
def about():
    return "Página sobre"  # Retorna uma resposta simples para a rota "/about"

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    app.run(debug=True)  # Inicia o servidor Flask com modo debug ativado
