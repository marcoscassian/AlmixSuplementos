from flask import Flask, render_template, url_for, request, flash, session, redirect
from flask_login import LoginManager, login_user, UserMixin, login_required
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')