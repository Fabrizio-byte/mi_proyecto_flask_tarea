# Se importan las clases necesarias de la biblioteca Flask
from flask import Flask

# Se crea una instancia de la aplicación Flask
app = Flask(__name__)

# Se define la primera ruta, que es la página de inicio
@app.route('/')
def home():
    # Retorna el texto que se mostrará en el navegador
    return '¡Hola, mundo!'

# Se define una ruta con un parámetro dinámico para un nombre
@app.route('/usuario/<nombre>')
def usuario(nombre):
    # Se retorna un saludo personalizado usando el nombre proporcionado en la URL
    return f'¡Bienvenido, {nombre}!'

# Este bloque se asegura de que la aplicación se ejecute
# solo cuando el script se ejecuta directamente
if __name__ == '__main__':
    # El método run() inicia el servidor de desarrollo
    # 'debug=True' permite la recarga automática al guardar cambios
    app.run(debug=True)
