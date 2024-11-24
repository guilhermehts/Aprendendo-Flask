#importação da biblioteca do Flask, com os métodos adicionados
#utilizando o comando "flask run" para rodar o app
from flask import Flask, request, jsonify, redirect, url_for, render_template, make_response

app = Flask(__name__)

#ROTA BÁSICA (GET)
@app.route('/')
def home():
    return "Bem-vindo à aplicação Flask."

#ROTA DINÂMICA COM PARÂMETRO NA URL
@app.route('/user/<username>')
def user_profile(username):
    return f"Perfil do Usuário: {username}"

#ROTAS DINÂMICAS COM TIPOS(int, float, path)
#int
@app.route('/order/<int:order_id>')
def order(order_id):
    return f"Detalhes do pedido número: {order_id}"

#float
@app.route('/price/<float:amount>')
def price(amount):
    return f"Preço: R$ {amount:.2f}"

#path
@app.route('/file/<path:filepath>')
def file_path(filepath):
    return f"Caminho do arquivo: {filepath}"

#ROTA COM MÚLTIPLOS MÉTODOS (GET e POST)
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form.get('data')
        return f"Dados recebidos: {data}"
    return '''
        <form method="post">
            <input type="text" name="data" placeholder="Insira algo">
            <button type="submit">Enviar</button>
        </form>
    '''
#ROTA COM JSON(API)
@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({"received": data}), 201
    return jsonify({"message": "Envie dados via POST"})

#ROTA PARA REDIRECIONAMENTO
@app.route('/redirect')
def redir():
    return redirect(url_for('home'))

#ROTA COM CABEÇALHOS PERSONALIZADOS
@app.route('/custom-header')
def custom_header():
    response = make_response("Resposta com cabeçalhos personalizados")
    response.header['Custom-Header'] = 'Valor do Cabeçalho'
    return response

#ROTA DE ERRO PERSONALIZADA
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Rota não encontrada"}),404

#ROTA PARA RENDERIZAÇÃO DE TEMPLATE
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

#ROTA COM SUBDOMÍNIOS
@app.route('/subdomain', subdomain='api')
def subdomain():
    return "Esta é uma rota em um subdomínio."

#ROTA COM PARÂMETROS DE CONSULTA(Query Parameters)
@app.route('/search')
def search():
    query = request.args.get('q', 'Nada buscado')
    return f"Resultado para a busca: {query}"

#ROTA COM UPLOAD DE ARQUIVOS
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f".uploads/{file.filename}")
    return f"Arquivo {file.filename} salvo com sucesso!"