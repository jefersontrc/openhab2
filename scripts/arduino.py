#!/usr/bin/python
# -*- coding: iso-8859-1 -*-


import time
import serial
import os
import sys
import paho.mqtt.client as mqtt

from time import sleep

broker= "172.16.1.130"
port = 1883

def on_publish(client, userdata, result):
    print("data plublished \n")
pass


#iniciando conexao serial
comport = serial.Serial('/dev/ttyACM0', 9600)
#comport = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # Setando timeout 1s para a conexao
 
#PARAM_CARACTER='t'
#PARAM_ASCII=str(chr(116))       # Equivalente 116 = t
 
# Time entre a conexao serial e o tempo para escrever (enviar algo)
time.sleep(1.8) # Entre 1.5s a 2s
 
#comport.write(PARAM_CARACTER)
#comport.write(PARAM_ASCII)
 
VALUE_SERIAL=comport.readline()
 
print '%s' % (VALUE_SERIAL)
num=float(VALUE_SERIAL)



client = mqtt.Client("nobreak")
client.on_publish = on_publish
client.connect(broker, port)
ret=client.publish("sensor/nobreak" ,num)

# Fechando conexao serial
comport.close()
