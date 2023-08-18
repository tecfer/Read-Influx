import subprocess
import sys
import pkg_resources

def install_requirements(requirements_file):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    except subprocess.CalledProcessError as e:
        print("Error al instalar las dependencias:", e)
        sys.exit(1)

def requirements_check():
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
        
        
    except FileNotFoundError:
        print(f"No se encontró el archivo {requirements_file}.")


def connet_bbdd(server_ip,server_port,key):
    print(f"ha seleccionado {key}")
    import influxdb
    try:
        client = influxdb.InfluxDBClient(host=server_ip, port=server_port, database=key)
        print("Conexión exitosa.")
        
        result = client.query("SHOW MEASUREMENTS;")
        print("---- SHOW MEASUREMENTS ----")
        lista = list(result.get_points())
        
        for idx, item in enumerate(lista):
            nombre = item['name']
            print(f"{idx} - {nombre}")
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")


def program():
    
    from dotenv import load_dotenv # pip install python-dotenv
    import requests
    import influxdb
    import os

    load_dotenv()

    server_ip = os.getenv('SERVER_IP')
    server_port = os.getenv('SERVER_PORT')

    client = influxdb.InfluxDBClient(server_ip,server_port,)
    databases = client.query("show databases;")

    print("Bases de datos:")    
    print('---------')

    databases_set = list(databases.get_points())

    for bbdd in databases_set:
        nombre = bbdd['name']
        print(f"{databases_set.index(bbdd)} - {nombre}")


    key = ''
    while key != 'q':
        try:
            key = input("Selecciona la BBDD 'q' para salir: ")
            index = int(key)
            if index in range(0,len(databases_set)):
                
                #connet_bbdd(index) 
                connet_bbdd(server_ip,server_port,databases_set[index]['name'],)   
                key = 'q'
        except:
            pass
   
    
    
if __name__ == "__main__":
    requirements_check()
    program()
