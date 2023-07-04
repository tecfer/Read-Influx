#pip install requests
import requests
#pip install influxdb
import influxdb

#pip install python-dotenv
from dotenv import load_dotenv

def connet_bbdd(key):
    print(f"ha seleccionado {key}")
    server_ip = os.getenv('SERVER_IP')
    server_port = os.getenv('SERVER_PORT')

    client = influxdb.InfluxDBClient(host=server_ip, port=server_port, database=key)
    result = client.query("SHOW MEASUREMENTS;")
    print("SHOW MEASUREMENTS")
    lista = list(result.get_points())
    for item in lista:
        nombre = item['name']
        print(f"{lista.index(item)} - {nombre}")


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
lista_bases_de_datos = list(resultado.get_points())

# Recorrer la lista e imprimir los nombres de las bases de datos
for base_de_datos in lista_bases_de_datos:
    nombre = base_de_datos['name']
    print(f"{lista_bases_de_datos.index(base_de_datos)} - {nombre}")


key = ''
while key != 'q':
    try:
        key = input("Selecciona la BBDD 'q' para salir: ")
        index = int(key)
        if index in range(0,len(lista_bases_de_datos)):
            
            #connet_bbdd(index) 
            connet_bbdd(lista_bases_de_datos[index]['name'])   
            key = 'q'
    except:
        pass
   
    
    
