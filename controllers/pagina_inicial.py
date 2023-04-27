from flask import Flask, render_template, redirect, url_for, Blueprint, request

pagina_inicial = Blueprint("pagina_inicial", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

# ------------- tela inicial do site ------------------
@pagina_inicial.route("pag_inicial")
def pag_inicial():
    return render_template("pagina-inicial/pag_inicial.html")