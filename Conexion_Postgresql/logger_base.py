import logging

'''
Desde aquí configuramos los mensajes logging
'''

logger = logging
logger.basicConfig(level=logger.DEBUG,
                   format='%(asctime)s: %(levelname)s %(message)s',
                   #    format='%(asctime)s: %(levelname)s [%(filename)s: linea- %(lineno)s] %(message)s',
                   # datefmt='%I:%M:%S %p',
                   handlers=[logging.FileHandler('C:\\DTUpdateFusion\\Log\\maxfa_fusion.log'),
                             logging.StreamHandler()
                             ])

######################################################################################################
# Cambio ruta para pc del fede
