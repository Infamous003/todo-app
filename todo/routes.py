from todo import app
from flask import render_template, url_for, flash, redirect, get_flashed_messages
from todo.forms import SignupForm, LoginForm
from todo.models import User
from todo import db
from flask_login import login_user, logout_user

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET","POST"])
def signup_page():
    form = SignupForm()
    if form.validate_on_submit():
        usr = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(usr)
        db.session.commit()
        login_user(usr)
        return redirect(url_for("home"))
    else:
        for error_msg in form.errors.values():
            flash(error_msg[0], category="danger")

    return render_template("signup.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user and user.verify_password(form.password.data):
            flash(f"Logged in as {user.name}", category="success")
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash(f"Username and password do not match", category="warning")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("home"))