from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired])
    password = PasswordField('Password', validators=[DataRequired])
    name = StringField('Name', validators=[DataRequired])
    btn_login = SubmitField('Login')