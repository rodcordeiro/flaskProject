from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

key = ''
@app.route('/')
@app.route('/index')
def index():
    print(key)
    user = {'username':'RodCordeiro'}
    posts =[
    {
        'author':{'username':'Jhon'},
        'body':'A beautiful day in Portland'
    },
    {
        'author':{'username':'Susan33'},
        'body':'Avengers movie: the truth about it'
    }
    ]
    return render_template('index.html',title="Cordeiro's DEV",user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        password_provided = form.password.data
        password = password_provided.encode() # Convert to type bytes
        salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/teste')
def teste():
    user = {'username':'RodCordeiro'}
    if key != '':
        dados [{'titulo':'CriptoTeste','login':'Funfo','senha':'gAAAAABecLcVHs4ds7jSy0gLGFz0QuhHfqLotLNTJwhTjX4s8rSkZiyFvWadjvmBGtXkgj3CF6vuJR1NJiuWcCGMSXz9HQ8QJF5oYJtYUqGJ8VTbmcxlGRg='}]
    else:
        dados = [{'titulo':'Teste','login': 'RodCordeiro','senha':'@C0rdeiro'},{'titulo':'Desenvolvimento','login':'cordeiro','senha':'master'},{'titulo':'MySQL','login':'cordeiro','senha':'@C0rdeiro'}]
    return render_template('teste.html',title="Cordeiro's DEV",user=user, info=dados)





@app.errorhandler(404)
def page_not_found(e):
    return render_template('erro.html'),404
