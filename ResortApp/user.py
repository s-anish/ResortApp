from cryptography.fernet import Fernet
import hashlib
from ResortApp import app
from flask import render_template, make_response, redirect, request
from ResortApp.dbutilities import guest_utilities
from functools import wraps


@app.route('/login', methods=['GET'])
def login():
    try:
        user_name = request.cookies.get('userID')
        return render_template("login.html", user_name=user_name)
    except:
        return render_template("login.html", user_name="")


@app.route('/login', methods=['POST'])
def set_cookie():
    user = request.form['user_name']
    email = request.form["email"]
    password = request.form["pass"]
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the string
    hash_object.update(password.encode())

    # Get the hexadecimal digest of the hash

    hash_hex = hash_object.hexdigest()
    role, message = guest_utilities.get_role(user, email, hash_hex)

    if role is None:
        return message
    else:
        resp = make_response(redirect('/'))
        resp.set_cookie('userID', user, 60*60*24)
        resp.set_cookie('role', role, 60*60*24)
        return resp


def role_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            get_role = request.cookies.get('role')
            i = 0
            for role in roles:
                if get_role == role:
                    i = 1
            if i == 1:
                return func(*args, **kwargs)
            return "You dont have Authorization"
        return wrapper
    return decorator


# def role_required(role):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             get_role = request.cookies.get('role')
#             if get_role != role:
#                 return 'Unauthorized access'
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


@app.route('/logout')
def logout():
    user = 'anish'
    role = 'guest'
    resp = make_response(redirect('/'))
    resp.set_cookie('userID', user, max_age=0)
    resp.set_cookie('role', role, max_age=0)
    return resp


