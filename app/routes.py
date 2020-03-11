from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
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

@app.route('/teste')
def teste():
    user = {'username':'RodCordeiro'}
    dados = [{'titulo':'Teste','login': 'RodCordeiro','senha':'@C0rdeiro'},{'titulo':'Desenvolvimento','login':'cordeiro','senha':'master'},{'titulo':'MySQL','login':'cordeiro','senha':'@C0rdeiro'}]
    return render_template('teste.html',title="Cordeiro's DEV",user=user, info=dados)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)




@app.errorhandler(404)
def page_not_found(e):
    return render_template('erro.html'),404
