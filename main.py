#Aqui va estar todo el codigo del programa 
import os
import getpass
from datetime import datetime
import json

#Esta funcion solo sera llamada si es que el usuario habre por primera ves el programa
#o por si no hay un archivo de configuracion donde esten alojados los datos

def first_init(): #Esta funcion confirmara si es la primera ves que se ejecuta o no
    #si es la primera ves que se ejecuta llamara la funcion create_json para crear el archivo
    #donde este guardado el username y la fecha
    username = getpass.getuser()
    archive_path = os.path.join(os.path.expanduser("~"), ".config", "hibirth", f"{username}_data.json")
    
    if not os.path.exists(archive_path):
        create_json()
    else:
        pass #Aqui en un futuro llamare a una funcion que se encarge de ya calcular los dias que faltan
    
def pedir_birth():
    # Aqui implementare la logica donde le pedire al usuario su fecha de cumpleaños
    while True:
        #Se le pide al usuario el birthday
        fecha = input("Introduce tu fecha de nacimiento DD/MM/YY (ejemplo: 31/12/2015): ") 
    
        
        try:
            #Comprobamos que la fecha este en el formato indicado
            datetime.strptime(fecha, '%d/%m/%Y')
            return fecha
        
        except ValueError:
            
            print("Formato no reconocido, por favor intentalo denuevo")

def create_json(): #Esta funcion creara el json donde estara guardado el nombre y la fecha 
    username = getpass.getuser() #conseguimos el nombre de usuario
    
    fecha = pedir_birth() #llamamos a la funcion pedir_birth
    
    datos = {
            "name" : f"{username}",
            "fecha" : f"{fecha}", 
    } #creamos un diccionario con los datos
    
    
    # Ruta de configuración: ~/.config/hibirth/hibirth-<usuario>.json
    config_dir = os.path.join(os.path.expanduser("~"), ".config", "hibirth") 
    os.makedirs(config_dir, exist_ok=True)  # Crea la carpeta si no existe
    
    # Ruta del archivo donde esten los datos
    archive_path = os.path.join(config_dir, f"{username}_data.json") #se nombra el archivo con el nombre de usuario
    #Ejemplo = home/user/.config/hibirth/user_data.json
    
    with open(archive_path, "w") as archive: #Abrimos el archivo (o lo crea), y lo nombramos archive
        json.dump(datos, archive, indent=4) #dumpeamos (escribimos) los datos en el archivo con sangria bonita
   

#pedir_birth() #Con esto pruebo que la funcion pedir_birth este correcta
create_json() #Probrar que la funcion funcione correectamente 
