# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, abort, make_response, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello from Flask!</p><table><tr><td><b>Aluno:</b></td><td>Leonardo Correia</td></tr><tr><td><b>Prontuário:</b></td><td>PT3026621</td></tr></table>'

#user
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

#contextorequisicao
@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent');
    return '<p>Your browser is {}</p>'.format(user_agent);

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
     abort(400)  # Força um erro 400

@app.errorhandler(400)
def bad_request(error):
    return 'Bad request', 400

#objetoresposta
@app.route('/objetoresposta')
def objetoresposta():
    resp = make_response("<h1>This document carries a cookie!</h1>")
    resp.set_cookie('answer', '4.2')
    return resp

#redirecionamento
@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')

#abortar
@app.route('/abortar')
def not_found():
    abort(404)  # Força um erro 404



