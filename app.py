# Importar la biblioteca
from flask import Flask , render_template

# Crear un servidor
app = Flask(__name__)

# Rutas (Principal)
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/pokemons-legendarios')
def legendario():
    return render_template("legendarios.html")


# Ejecuta el servidor.
app.run(debug=True)
