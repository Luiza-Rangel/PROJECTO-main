from flask import Flask, render_template
from model.produtos import select
app = Flask(__name__)

@app.route("/")
def pg_inicial():
    itens = select()
    return render_template("index.html", itens=itens)

@app.route("/pagina2")
def segunda_pag():
    itens = select()
    return render_template("pagina2.html", itens=itens)

app.run(debug=True)