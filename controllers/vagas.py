from flask import Flask, render_template, redirect, url_for, Blueprint, request

vagas = Blueprint("vagas", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

#       --------------- interface para dispositivos IoT -----------------

@vagas.route("index_vagas")
def index_vagas():
    return render_template("vagas/vagas.html")