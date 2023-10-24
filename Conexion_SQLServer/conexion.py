import pyodbc
from Conexion_SQLServer.logger_base import logger

class SQLServer:
    def __init__(self, username=None, password=None):
        self.server = 'XXXXXXXXX;'
        self.database = 'XXXXXXXXXX;'
        if username != None:
            self.username = f'UID={username};'
        else:
            self.username = None
        if password != None:
            self.password = f'PWD={password};'
        else:
            self.password = None
        self.connection = None

    def __enter__(self):
        try:
            # Conexion con usuario y contraseña
            if self.username != None and self.password != None:
                self.connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + self.username + self.password + 'DATABASE=' + self.database)
            else:
            # Conexion sin usuario y contraseña
                self.connection = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + 'DATABASE=' + self.database + 'Trusted_Connection=yes;')
            return self.connection.cursor()
            logger.debug(f'Conexion exitosa')
        except Exception as e:
            logger.error(f'Conexion fallida: {e}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is not None:
                self.connection.rollback()
                print("Error occurred: ", str(exc_val))
            else:
                self.connection.commit()
            self.connection.close()


if __name__ == "__main__":
    with SQLServer() as cursor:
        cursor.execute('Select * from [BaseDatos].[dbo].[Tabla]')
        for i in cursor.fetchall():
            print(i)
