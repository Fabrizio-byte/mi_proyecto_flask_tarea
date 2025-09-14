import sqlite3

class DatabaseManager:
    def __init__(self, db_name='inventario.db'):
        self.db_name = db_name
        self._crear_tabla_productos()

    def _crear_tabla_productos(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    # Métodos para insertar, actualizar, eliminar y obtener productos...
    # (Aquí debes añadir el resto de los métodos que se mostraron en la respuesta anterior)