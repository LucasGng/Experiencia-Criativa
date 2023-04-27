from flask import Flask, render_template, url_for
from controllers.login import login
from controllers.pagina_inicial import pagina_inicial
from controllers.vagas import vagas
from controllers.servico import servico


app = Flask(__name__, template_folder="./views/", static_folder="./static/")

#       --------------- registrando blueprints-----------------

app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(pagina_inicial, url_prefix='/pagina_inicial')
app.register_blueprint(vagas, url_prefix='/vagas')
app.register_blueprint(servico, url_prefix='/servico')

#       --------------- base -----------------

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)
#sssssssssss