from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired("Por favor, preencha aqui")])
    password = PasswordField('Password', validators=[
                             DataRequired("Por favor, preencha aqui")])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')


class ContatoForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired("Por favor, preencha aqui")])
    text = TextAreaField('Text', description="Escreva algo para nós! :)", validators=[
                         DataRequired("Por favor, preencha aqui")])
    submit = SubmitField('Enviar')
