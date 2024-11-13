from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class SignupForm(FlaskForm):
    name = StringField(label="Username", validators=[DataRequired(), Length(max=20)])
    email = StringField(label="Email", validators=[DataRequired(), Length(max=30)])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=6, max=16)])
    confirm_password = PasswordField(label="Confirm password", validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label="submit")

class LoginForm(FlaskForm):
    name = StringField(label="Username", validators=[DataRequired(), Length(max=20)])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=6, max=16)])
    submit = SubmitField(label="Login")