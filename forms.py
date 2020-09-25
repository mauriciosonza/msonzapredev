from flask_wtf import FlaskForm,RecaptchaField,Recaptcha
from wtforms import StringField, FileField, SubmitField,BooleanField,RadioField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import Length
from wtforms_components import ColorField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Login!')