from flask import Flask, render_template

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

