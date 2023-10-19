from Conexion.conexion import Conexion
from Conexion.logger_base import logger

class CursorDelPool():
    '''
    CursorDelPool: En esta clase se configura con los metodos __enter__ y __exit__, como queremos
    que funcione with con esta clase.
    Se crean objetos, y a partir del objeto creado se asigna una conexion y un cursor.
    Se crean varios objetos por cada usuario que solicite una conexion,
    desde aca se administra la conexion real a la base de datos.
    '''
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def __enter__(self):
        # logger.debug('X'.center(49,'X'))
        # logger.debug(f'Inicio de with metodo __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor

    def __exit__(self, tipo_error, valor_error, mensaje_error):
        # logger.debug(f'Se ejecuta el metodo __exit__()')

        if valor_error:
            self.__conn.rollback()
            logger.error(f'Ocurrio una excepcion, rollback: {valor_error}')
        else:
            self.__conn.commit()
            # logger.debug(f'Commit de la transaccion')

        self.__cursor.close()
        Conexion.liberarConexion(self.__conn)

if __name__ == '__main__':
    # Obtener cursor a partir de la conexion del pool
    # with ejecuta primero metodo enter y termina con exit de manera automatica
    # si no usamos with para inicializar, entonces no se inicializan las variables
    with CursorDelPool() as cursor:
        # automaticamente ejecuta el metodo enter y nos devuelve un cursor
        # cursor.execute("INSERT INTO dbo.d_banco(bco_desc, bco_fcregistracion, fc_modificacion) VALUES ('prueba', '2023-05-20', '2023-05-20');")
        cursor.execute('SELECT * FROM dbo.d_banco')
        print('Listado de bancos')
        print(cursor.fetchall())
