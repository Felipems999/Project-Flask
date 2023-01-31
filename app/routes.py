from app import app
from app.forms import LoginForm, ContatoForm
from flask import render_template, flash as fl, redirect as rdct, url_for as url


@app.route('/')
@app.route('/index')
def index():

    user = {'username': 'Melissa'}
    posts = [{
        'author': 'Felipe',
        'text': 'Aprendendo Python Flask, um microframework para criar webapp',
        'date': '22/01/2023'
    },
        {
            'author': 'Melissa',
            'text': 'Visitando hospital na aula de hoje!',
            'date': '20/01/2023'
    },
        {
            'author': 'Flávio',
            'text': 'Primeiro dia de aula',
            'date': '1 ano atrás'
    }]

    return render_template('index.html', title='home page', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if (form.validate_on_submit()):
        fl(f'Requisição de login para {form.username.data}, remember_me = {form.remember_me.data}')
        return rdct(url('index'))

    return render_template('login.html', title='Logar', form=form)


@app.route('/contato')
def contato():
    form = ContatoForm()

    if (form.validate_on_submit()):
        fl('Sua mensagem foi enviada. Obrigado!!!')
        return rdct(url('contato'))

    return render_template('contato.html', title='Contato', form=form)


@app.route('/about')
def about():
    desc = 'Este é um microblog em desenvolvimento'

    return render_template('about.html', description=desc)
