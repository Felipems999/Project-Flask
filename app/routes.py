from app import app
from flask import render_template


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
    }]

    return render_template('index.html', title='home page', user=user, posts=posts)
