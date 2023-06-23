#pip install requests
import requests
#pip install influxdb
import influxdb

#pip install python-dotenv
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

import os

server_ip = os.getenv('SERVER_IP')
server_port = os.getenv('SERVER_PORT')

client = influxdb.InfluxDBClient(server_ip,server_port,)
resultado = client.query("show databases;")

print("Bases de datos:")
#for row in resultado:

print('---------')
lista_bases_de_datos = resultado.get_points()

# Recorrer la lista e imprimir los nombres de las bases de datos
for base_de_datos in lista_bases_de_datos:
    nombre = base_de_datos['name']
    print(nombre)
