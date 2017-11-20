from flask import Flask, render_template, request # importa os metodos da classe Flask
from pessoa import Pessoa # importa a classe Pessoa

app = Flask('webApp') # Instancia a classe Flask no Objeto webapp, lembrando que está "webapp" pois é o nome do meu arquivo .py principal e poderia ser qualquer nome

p = Pessoa() # cria uma instancia da classe Pessoa

@app.route('/') # define as rotas
def layout(): # metodo que exibe a tela Inicial 'Visualizar.html'
    return render_template('visualizar.html')

@app.route('/cadastro', methods=['POST', 'GET']) # define a rota passando o metodo GET e POST
def cadastro(): # metodo que realiza o "cadastro" do usuario
    if request.method == 'POST':  # se o metodo vier por POST ele pega todos os dados que vier do formulario e salva na classe Pessoa
        dados_dict = request.form.to_dict() #salva todos os dados do formulario da pagina /cadastro dentro da variavel "dados_dict"
        p.set_pessoa(dados_dict) # passa por parametro a variavel dados_dict para a função set_pessoa da classe pessoa
        return render_template('visualizar.html', parent_dict = p.get_pessoa()) # exibe a pagina visualizar passando uma Lista de dicionarios

    return render_template('cadastro.html')

@app.route('/visualizar')
def visualizar():
    return render_template('visualizar.html', parent_dict = p.get_pessoa() )

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/index')
def index():
    p.get_pessoas()

    return render_template('index.html')

app.run(debug=True, use_reloader=True) #utililado para iniciar o servidor -> abra o cmd e digite "python C:\caminho do arquivo"
