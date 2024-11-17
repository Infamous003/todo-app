from todo import app
from flask import render_template, url_for, flash, redirect, get_flashed_messages
from todo.forms import SignupForm, LoginForm, CreateTaskForm
from todo.models import User, Task
from todo import db
from flask_login import login_user, logout_user, current_user

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET","POST"])
def signup_page():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
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
            return redirect(url_for("user_page", userid=user.user_id))
        else:
            flash(f"Username and password do not match", category="warning")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("home"))

@app.route("/user/<int:userid>")
def user_page(userid):
    user = User.query.filter_by(user_id=userid).first()
    user_tasks = Task.query.filter_by(user_id=user.user_id).all()
    return render_template("user.html",user=user, user_tasks=user_tasks)

@app.route("/complete_task/<int:task_id>")
def complete_task(task_id):
    task_completed = Task.query.filter_by(task_id=task_id).first()
    task_completed.status = 1
    db.session.add(task_completed)
    db.session.commit()
    flash("You're doing great! Keep it up!", category="success")

    return redirect(url_for("user_page", userid=current_user.user_id))


@app.route("/remove/<int:task_id>")
def remove_task(task_id):
    task_to_remove = Task.query.filter_by(task_id=task_id).first()
    db.session.delete(task_to_remove)
    db.session.commit()
    flash("Task has been removed.", category="warning")

    return redirect(url_for("user_page", userid=current_user.user_id))


@app.route("/create_task", methods=["POST", "GET"])
def create_task_page():
    form = CreateTaskForm()
    if form.validate_on_submit():
        task = Task.query.filter_by(name=form.name.data).first()
        if task:
            flash("You already have the same task pending.", category="warning")
        else:
            newTask = Task(name=form.name.data, description=form.name.data, user_id=current_user.user_id)
            db.session.add(newTask)
            db.session.commit()
            flash(f"Task added!", category="success")
            return redirect(url_for("user_page", userid=current_user.user_id))
    return render_template("create_task.html", form=form)
