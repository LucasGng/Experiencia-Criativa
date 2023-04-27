from flask import Flask, render_template, redirect, url_for, Blueprint, request

servico = Blueprint("servico", __name__, template_folder='./views/', static_folder='./static/', root_path="./")
saved_servico = {}
saved_data = {}

#       --------------- registra serviço -----------------

@servico.route("registro_form")
def registro_form():
    return render_template("registrar-servico/registrar_servico.html")

@servico.route("registro_action", methods=['GET', 'POST'])
def registro_action():
    global saved_servico
    global saved_data
    if request.method == "POST" :

        serviço = request.form.get("serviço")

        data = request.form.get("data")

    id = len(saved_servico)+1
    saved_servico[id] = "Serviço: " + serviço
    saved_data[id] = "Data: "+ data

    return render_template("index.html")

#       --------------- print dos serviços registrados -----------------

@servico.route("registro_list")
def registro_list():
    return render_template("registrar-servico/registro_list.html", servicos = saved_servico, datas = saved_data)
