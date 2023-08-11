#pip install requests
import requests
#pip install influxdb
import influxdb

'''
Ejemplo de try import
try:
    import requests
except ImportError:
    print("El módulo 'requests' no está instalado.")
    install_requests = input("¿Deseas instalarlo ahora? (s/n): ")
    if install_requests.lower() == 's':
        try:
            import subprocess
            subprocess.check_call(['pip', 'install', 'requests'])
            print("El módulo 'requests' se ha instalado correctamente.")
        except Exception as e:
            print("Ha ocurrido un error al intentar instalar 'requests':", e)
    else:
        print("No se ha instalado el módulo 'requests'.")
else:
    print("El módulo 'requests' está instalado.")

'''

'''

Ejemplo de try requirements
import subprocess
import sys

def install_requirements(requirements_file):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    except subprocess.CalledProcessError as e:
        print("Error al instalar las dependencias:", e)
        sys.exit(1)

def main():
    requirements_file = "requirements.txt"
    try:
        with open(requirements_file, "r") as f:
            required_packages = [line.strip() for line in f.readlines()]
        
        installed_packages = [pkg.key for pkg in pkg_resources.working_set]
        missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages]

        if missing_packages:
            print("Faltan dependencias:")
            for pkg in missing_packages:
                print(f"- {pkg}")
            install = input("¿Deseas instalar las dependencias faltantes? (s/n): ")
            if install.lower() == 's':
                install_requirements(requirements_file)
        else:
            print("Todas las dependencias están instaladas.")
        
        # Aquí puedes ejecutar tu archivo Python
        # por ejemplo:
        # import tu_archivo
    except FileNotFoundError:
        print(f"No se encontró el archivo {requirements_file}.")

if __name__ == "__main__":
    main()

'''

#pip install python-dotenv
from dotenv import load_dotenv

def connet_bbdd(key):
    print(f"ha seleccionado {key}")
    server_ip = os.getenv('SERVER_IP')
    server_port = os.getenv('SERVER_PORT')

    client = influxdb.InfluxDBClient(host=server_ip, port=server_port, database=key)
    result = client.query("SHOW MEASUREMENTS;")
    print("----SHOW MEASUREMENTS----")
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
   
    
    
