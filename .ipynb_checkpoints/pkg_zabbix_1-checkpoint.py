#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

__author__ = rotoapanta
__copyright__ = "Copyright 2021, BitTech"
__credits__ = ["Roberto Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__fecha__ = Sun Apr 23 20:32:12 2023
__description__ = "Paquete para establece una conexión con un servidor Zabbix y devuelve un objeto ZabbixSender para enviar datos."

"""
from pyzabbix import ZabbixSender

def connect2zabbix(zx_ip, zx_port):
    '''
    Establece una conexión con un servidor Zabbix y devuelve un objeto ZabbixSender para enviar datos.
    
    Parameters
    ----------
    zx_ip : str
        La dirección IP del servidor Zabbix.
    zx_port : int
        El número de puerto en el que se debe establecer la conexión con el servidor Zabbix.

    Raises
    ------
    
    Exception
        Si no se puede establecer una conexión con el servidor Zabbix.

    Returns
    -------
    
     ZabbixSender
        Un objeto ZabbixSender que se utilizará para enviar datos al servidor Zabbix.

    '''
    try:
        return ZabbixSender(zx_ip, zx_port)
    except Exception as e:
        raise ("Error in connect2zabbix: %s" % str(e))
        
connect2zabbix('192.168.1.115', 10051)
