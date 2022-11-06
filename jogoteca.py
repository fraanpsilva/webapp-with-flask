from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista_de_jogos = [jogo1, jogo2, jogo3]


app = Flask(__name__)

@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogo', jogos = lista_de_jogos)

@app.route('/novo-jogo')
def novoJogo():
    return render_template('novo-jogo.html', titulo= 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criaJogo():
    # capturando as informações do formulario
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    # criando um objeto com as informações do formulário
    jogo = Jogo(nome, categoria, console)

    # adicionando na lista de jogos
    lista_de_jogos.append(jogo)

    return render_template('lista.html', titulo= 'Jogos', jogos=lista_de_jogos)

app.run(debug=True)
# trecho da app caso quiser alterar a porta
# app.run(host='0.0.0.0', port=8080)