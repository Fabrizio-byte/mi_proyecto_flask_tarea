from flask import Flask
from Conexión.conexion import db # Asegúrate de que la ruta de importación sea correcta

app = Flask(__name__)

@app.route('/')
def index():
    return "¡Hola desde Flask!"

@app.route('/test_db') # ¡Verifica que esta ruta coincida con la que escribes en el navegador!
def test_db():
    try:
        db.connect()
        return "Conexión a la base de datos exitosa."
    except Exception as e:
        return f"Error al conectar a la base de datos: {e}"
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)