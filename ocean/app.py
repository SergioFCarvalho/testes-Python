from flask import Flask
from flask import render_template

app = Flask("Meu App")

posts = [
    {
        "titulo":"Primeira post",
        "texto": "teste"
    },
    {
        "titulo": "Segundo post",
        "texto": "teste2"
    },
    
]

@app.route('/')
def exibir_entradas():
    entradas = posts
    return render_template('exibir_entradas.html', entradas=entradas)

