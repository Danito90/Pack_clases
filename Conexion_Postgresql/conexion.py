import sys
from psycopg2 import pool
from Conexion_Postgresql.logger_base import logger

class Conexion:
    '''
    Clase Conexion: Sus metodos estaticos, realizan la conexion a la base de datos.
    Con el pool de conexiones, creamos objetos para cada conexion, en este caso el maximo es 5 objetos.
    A medida que cada objeto conexion se desocupa, se libera un lugar.
    '''
    _DATABASE = 'XXXXXXXXXXX'
    _USERNAME = 'XXXXXXXXXXXXXXXXX'
    _PASSWORD = 'XXXXXXXXXX'
    _DB_PORT = '16421'
    _HOST = 'XXXXXXXXXXXXXXXXXXX'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    _usadas = 0

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                cls._MIN_CON, cls._MAX_CON,
                host=cls._HOST,
                user=cls._USERNAME,
                port=cls._DB_PORT,
                database=cls._DATABASE,
                password=cls._PASSWORD
                )
                return cls._pool
            except Exception as e:
                logger.error(f'Error al obtener pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool con exito')
        return conexion

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        if cls._pool != None:
            cls._usadas += 1
        else:
            usadas = 0
        libres = cls._pool.maxconn - cls._usadas

        logger.debug(f'Conexion obtenida del pool con exito en Postgresql: Libres {libres}')
        return conexion

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        #logger.debug(f'Pool cerrado')

if __name__ == '__main__':
    # en este caso la conexion1 toma un objeto de conexion y luego lo cierra. Al objeto 2
    # le asignan el mismo objeto ya que la conexion1 ya lo desocupo
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion1 = Conexion.obtenerConexion()
