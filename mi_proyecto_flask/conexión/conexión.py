import mysql.connector
from mysql.connector import errorcode

class DB:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'tu_contraseña_de_mysql'
        self.database = 'desarrollo_web'
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexión a la base de datos exitosa.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: El usuario o la contraseña son incorrectos.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: La base de datos no existe.")
            else:
                print(err)

    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexión a la base de datos cerrada.")

db = DB()