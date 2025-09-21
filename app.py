from flask import Flask, render_template, url_for, request, flash, session, redirect
from flask_login import LoginManager, login_user, UserMixin, login_required
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

card = [
    {
        "titulo": "Creatina 500g Refil",
        "preco": "R$ 120,00",
        "precoalt": "R$ 110,00 no Pix",
        "desconto": "10% OFF",
        "imagem": "static/img/creatina500.webp"
    },
    {
        "titulo": "Creatina 300g",
        "preco": "R$ 80,00",
        "precoalt": "R$ 75,00 no Pix",
        "desconto": "5% OFF",
        "imagem": "creatina300.jpg"
    },
    {
        "titulo": "Pré-Treino",
        "preco": "R$ 90,00",
        "precoalt": "R$ 85,00 no Pix",
        "desconto": "5% OFF",
        "imagem": "pretreino.jpg"
    },
    {
        "titulo": "Whey Protein Concentrado",
        "preco": "R$ 150,00",
        "precoalt": "R$ 140,00 no Pix",
        "desconto": "10% OFF",
        "imagem": "whey.jpg"
    }
]

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', cards=card)

#marcoslindoo