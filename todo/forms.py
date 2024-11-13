from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class SignupForm(FlaskForm):
    name = StringField(label="Username", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm password", validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label="submit")
