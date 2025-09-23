from flask import Flask, render_template, url_for, request, flash, session, redirect
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user
from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


from models import (
    db,
    Usuarios,
    Produtos
    )

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #define a url do banco de dados sqlite
db.init_app(app) #inicializa o db

bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()

app.secret_key = 'marcoslindo'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    produtos = Produtos.query.order_by(Produtos.id.desc()).all()
    
    return render_template('dashboard.html', produtos=produtos)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuarios.query.filter_by(email=email).first()

        if usuario and bcrypt.check_password_hash(usuario.senha, senha):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Email ou senha inválidos.', category='error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    
    if request.method == 'POST':
        nome = request.form.get('name') 
        email = request.form.get('email')
        senha = request.form.get('password')
        confirm = request.form.get('confirm_password')
        if senha != confirm:
            flash("As senhas não coincidem.", "error")
            return redirect(url_for('cadastro_usuario'))
        
        user_exists = Usuarios.query.filter_by(email=email).first()
        if user_exists:
            flash("Este email já está cadastrado.", "error")
            return redirect(url_for("cadastro_usuario"))
        
        senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

        novo_usuario = Usuarios(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()
            
        flash('Cadastro realizado com sucesso! Agora faça login.', 'success')
        return redirect(url_for('login'))
    return render_template('cadastro_usuario.html')

@app.route('/cadastrar_produto', methods=['GET', 'POST'])
@login_required
def cadastrar_produto():
        
    if request.method == 'POST':
        nome = request.form.get('name') 
        preco = request.form.get('preco')
        descricao = request.form.get('descricao')

        if not nome or not preco or not descricao:
            flash('Preencha todos os campos.', 'error')
            return redirect(url_for('cadastrar_produto'))
    
        novo_produto = Produtos(nome=nome, preco=preco, descricao=descricao)
        db.session.add(novo_produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('cadastrar_produto.html')

@app.route('/editar_produto/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_produto(id):
    produto = Produtos.query.get_or_404(id)

    if request.method == 'POST':
        produto.nome = request.form.get('nome')
        produto.descricao = request.form.get('descricao')
        produto.preco = request.form.get('preco')

        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for('dashboard'))

    return render_template('editar_produto.html', produto=produto)

@app.route('/excluir_produto/<int:id>', methods=['POST'])
@login_required
def excluir_produto(id):
    produto = Produtos.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash("Produto excluído com sucesso!", "success")
    return redirect(url_for('dashboard'))

from flask_login import logout_user, login_required

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('index'))

