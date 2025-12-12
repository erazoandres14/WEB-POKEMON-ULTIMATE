# Importar la biblioteca
from flask import Flask , render_template

# Crear un servidor
app = Flask(__name__)

# Rutas (Principal)
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return 'Esta es la ruta de about 😎'


# Ejecuta el servidor.
app.run(debug=True)