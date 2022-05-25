import imp
from flash import Flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import re

from flask import flash, redirect, request

@app.route("/")
def index():
    users = User.get_all_users()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/add_user")
def add_user_page():
    return render_template("add_user.html")

@app.route("/create_user", methods=['post'])
def create_user():
    if not User.validate_user(request.form):
        return redirect("/add_user")
    user = User.create(request.form)
    return redirect("/")

@staticmethod
def validate_user(user_info):
    is_valid = True
    if len(user_info['first_name']) < 3:
        flash("First_name needs to be greater than 3 characters!")
        is_valid = False
    if len(user_info['last_name']) < 3:
        is_valid = False
    if not EMAIL_REGEX.match(user_info['email']):
        flash("Email is invalid")
        is_valid=False
    return is_valid
