from Conexion_SQLServer.conexion import SQLServer
from Conexion_SQLServer.logger_base import logger


class Sentencias:
    class Sentencias:
        @classmethod
        def select(cls, consulta, usuario=None, clave=None):
            try:
                conexion = SQLServer(usuario, clave)
                conn = conexion.conexion()
                df = pd.read_sql_query(consulta, conn)

                # Codigo

            except Exception as e:
                logger.error(f'Error al acceder a la consulta select: {e}')

if __name__ == '__main__':
    sql = 'Select * from [CaldenOil.Net].[dbo].[Gastos_Maxfa]'
    for i in Sentencias.select(sql):
        print(i)
