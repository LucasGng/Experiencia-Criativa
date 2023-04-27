from flask import Flask, render_template, redirect, url_for, Blueprint, request

login = Blueprint("login", __name__, template_folder='./views/', static_folder='./static/', root_path="./")
saved_login = []
saved_password = []

#       --------------------login--------------------

@login.route("login_form")
def login_form():
    return render_template("login/login.html")

@login.route("login_action", methods=['GET', 'POST'])
def login_action():
    validated_login = False
    validated_password = False
    if request.method == "POST" :

        email = request.form.get("email")

        password = request.form.get("password")

    if password and email:

        if password in saved_password:
            validated_password = True

        if email in saved_login:
            validated_login = True

    if validated_login == True and validated_password == True:
        return render_template("index.html")

#      ------------------register-------------------

@login.route("register_form")
def register_form():
    return render_template("login/register.html")

@login.route("register_action", methods=['GET', 'POST'])
def register_action():
    global saved_login
    global saved_password
    if request.method == "POST" :

        email = request.form.get("email")

        password = request.form.get("password")

    
        saved_login.append(email)

    
        saved_password.append(password)

    return render_template("login/login.html")


@login.route("usuario_list")
def usuario_list():
    return render_template("login/usuarios_list.html", usuarios = saved_login)
