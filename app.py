# Importa la clase Flask y la función render_template
from flask import Flask, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define la ruta para la página de inicio
@app.route('/')
def home():
    # Renderiza la plantilla index.html
    return render_template('index.html')

# Define la ruta para la página "Acerca de"
@app.route('/about')
def about():
    # Renderiza la plantilla about.html
    return render_template('about.html')

# Inicia la aplicación en modo de depuración si el script se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)


