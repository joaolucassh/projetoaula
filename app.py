from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def inicial():
    return render_template('inicial.html')

@app.route("/usuario")
def usuario():
    return render_template('usuario.html')

@app.route("/anuncios")
def anuncios():
    return render_template('anuncios.html')

@app.route("/usuario/cadastro")
def cadastro():
    return render_template('cadastro.html')
