# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>Avaliação contínua: Aula 030</h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/user/Leonardo Correia/PT3026621/IFSP">Identificação</a></li>
            <li><a href="/contexto_requisicao">Contexto da requisição</a></li>
        </ul>
    '''


@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return f'''
        <h1>Avaliação contínua: Aula 030</h1>
        <h2>Aluno: {name}</h2>
        <h2>Prontuário: {prontuario}</h2>
        <h2>Instituição: {instituicao}</h2>
        <p><a href="../../../">Voltar</a></p>
    '''

# Rota para Contexto da Requisição
@app.route('/contexto_requisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')  # Navegador do cliente
    remote_ip = request.remote_addr  # IP do cliente
    host = request.host  # Host da aplicação

    return f'''
    <h1>Contexto da Requisição</h1>
    <p>Seu navegador é: {user_agent}</p>
    <p>O IP do computador remoto é: {remote_ip}</p>
    <p>O host da aplicação é: {host}</p>
    <a href="/">Voltar</a>
    '''