#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = serial_port_detected.py
__author__ = rotoapanta "Roberto Toapanta"
__copyright__ = "Copyright 2021, BitTech"
__credits__ = ["Roberto Toapanta, Giovanny Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__fecha__ = 4/2/22 22:25
__description__ = "Puertos seriales conectados y selección del puerto Prolific"
__information__ : https://qastack.mx/programming/12090503/listing-available-com-ports-with-python
"""

import serial.tools.list_ports

def detect_serial_port():
    """
    Detectar el puerto serial al que se conecta automáticamente
    """
    com_ports = serial.tools.list_ports.comports()
    for port in com_ports:
        # /dev/cu.usbserial-145240
        if 'USB' in port.description:
            return port.device
        if 'cu.usb' in port.description:
            return port.device
    return None

# serial_port = detect_serial_port() llamar a la funciopn y devuelve el puerto


def get_data_acquisition():
    serial_port_connected = detect_serial_port()  # Puerto de lectura o escritura.
    BAUD_RATE = 9600  # Velocidad de transmisión
    serial_port = serial.Serial(serial_port_connected,
                                BAUD_RATE,
                                timeout=1.0)  # Abrir el puerto serial, se establece un tiempo de espera de 1 seg
    print("Conectado a: " + serial_port.portstr)

    while True:
        try:
            raw_data = serial_port.readline()  # Leer una línea terminada '\n'
            # print(raw_data)
            if not raw_data:
                print("Desconectado Interfaz Serial")
                continue  # Si quiere acabar el proceso poner break
            values = str(raw_data[0:len(raw_data)].decode("utf-8"))
            list_values = values.split(',')
            return list_values
        except KeyboardInterrupt:
            print("Comunicación Serial Interrumpida")
            break

    serial_port.close()  # cierre el puerto inmediatamente.