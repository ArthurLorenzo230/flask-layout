from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title="Home")


@app.route("/boletim")
def boletim():
    return render_template('boletim.html', title="Boletim")


@app.route("/sobre-mim")
def sobre_mim():
    foto_url = "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80"
    return render_template('sobre_mim.html', title="Sobre mim", foto_url=foto_url)


@app.route('/validacao', methods=['GET', 'POST'])
def validacao():
    nome = ""
    sobrenome = ""
    idade = 0
    pode_votar = False
    pode_dirigir = False

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        sobrenome = request.form.get('sobrenome', '').strip()
        idade = int(request.form.get('idade', 0) or 0)

        pode_votar = idade >= 18
        pode_dirigir = idade >= 18

    return render_template(
        'validacao.html',
        title='Validação',
        nome=nome,
        sobrenome=sobrenome,
        idade=idade,
        pode_votar=pode_votar,
        pode_dirigir=pode_dirigir
    )

