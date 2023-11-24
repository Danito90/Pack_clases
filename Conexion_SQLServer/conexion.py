import pandas as pd
from sqlalchemy import create_engine

from Logger.logger_base import logger


class SQLServer:
    def __init__(self, username=None, password=None):
        # Conexion a notebook mia
        self.server = 'SERVER01'
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.database = 'XXXXXXX'
        if username != None:
            self.username = f'{username}'
        else:
            self.username = None
        if password != None:
            self.password = f'{password}'
            self.server = 'SERVER02'
        else:
            self.password = None

    def conexion(self):
        try:
            # Conexion con usuario y contraseña
            if self.username != None and self.password != None:
                SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{self.username}:{self.password.replace('@', '%40')}@{self.server}/{self.database}?driver={self.driver}"
            else:
                # Conexion sin usuario y contraseña
                SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{self.server}/{self.database}?driver={self.driver}&Trusted_Connection=yes"
            engine = create_engine(SQLALCHEMY_DATABASE_URI)
            connection = engine.connect()
            logger.debug(f'Conexion exitosa a SQL Server')
            return connection
        except Exception as e:
            logger.error(f'Conexion fallida a SQL Server: {e}')


if __name__ == "__main__":
    conexion = SQLServer()
    conn = conexion.conexion()
    df = pd.read_sql_query(sql, conn)
    print(df)
