from Conexion_SQLServer.conexion import SQLServer
from Conexion_SQLServer.logger_base import logger


class Sentencias:
    @classmethod
    def select(cls, consulta):
        try:
            with SQLServer('user', 'pass') as cursor:
            with SQLServer() as cursor:
                cursor.execute(consulta)
                registros = cursor.fetchall()
                filas = len(registros)
                columnas = len(registros[0])
                lista = []
                for fila in registros:
                    temp=[]
                    for item in range(0,columnas):
                        temp.append(str(fila[item]))

                    lista.append(temp)
                return lista
        except Exception as e:
            logger.error(f'Error al acceder a la consulta select: {e}')

if __name__ == '__main__':
    sql = 'Select * from [BaseDatos].[dbo].[Tabla]'
    for i in Sentencias.select(sql):
        print(i)
