from todo import app
from flask import render_template, url_for, flash, redirect
from todo.forms import SignupForm
from todo.models import User
from todo import db

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET","POST"])
def signup_page():
    form = SignupForm()
    # print(form.errors)
    if form.validate_on_submit():
        usr = User(name=form.name.data, email=form.email.data, password_hash=form.password.data)
        db.session.add(usr)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("signup.html", form=form)