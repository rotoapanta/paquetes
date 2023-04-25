#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__author__ = "Roberto Toapanta"
__copyright__ = "Copyright 2023, BitTech"
__credits__ = ["Roberto Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__fecha__ = 25/03/23 00:14
__description__ = "Comunicación Serial a Inclinómetro Digital"
"""

import serial

if __name__ == '__main__':
    list_values = []
    value = []

    #SERIAL_PORT = "/dev/ttyUSB0"  # puerto de lectura o escritura.   # linux
    #SERIAL_PORT = "/dev/cu.usbserial-145240"    # mac
    SERIAL_PORT = "COM5"  # puerto de lectura o escritura.   # win
    BAUD_RATE = 9600  # velocidad de transmisión
    PARITY = serial.PARITY_NONE
    STOP_BITS = serial.STOPBITS_ONE
    BYTE_SIZE = serial.EIGHTBITS

    serialPort = serial.Serial(
        port = SERIAL_PORT, # Puerto serial
        baudrate = BAUD_RATE, # Velocidad de baudios
        parity = PARITY,
        stopbits = STOP_BITS,
        bytesize = BYTE_SIZE,
        timeout = 1.0
    )

print("Conectado a: " + serialPort.portstr)

while True:
    try:
        raw_data = serialPort.readline()        # leer una línea terminada '\n'
        print(raw_data)
        if not raw_data:
            print("Desconectado Interfaz Serial")
            continue  # si quiere acabar el proceso poner break
        values = str(raw_data[0:len(raw_data)].decode("utf-8"))
        list_values = values.split(',')
        value_0 = (list_values[0])
        value_1 = (list_values[1])
        value_2 = (list_values[2])
        value_3 = (list_values[3])
        print(value_0[1:])           # 1er dato eje X
        print(value_1)          # 2do dato eje Y
        print(value_2)          # 3er dato temperatura
        print(value_3)          # 4to dato numero serial

    except KeyboardInterrupt:
        print("Comunicación Serial Interrumpida")
        break
serialPort.close()          # cierre el puerto inmediatamente.

