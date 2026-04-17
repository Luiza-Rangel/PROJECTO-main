from flask import Flask, render_template, request, redirect
from model.produtos import mostrar_comidas, rec_destaque
from model.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    comidas = mostrar_comidas()
    return render_template("index.html", exibir_comidas=comidas)

@app.route("/produto")
def segunda_pagina():
    return render_template("produto.html")


@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usuario = Usuario(usuario, senha, nome)
    novo_usuario.cadastrar()

    return redirect("/")

app.run(debug=True)