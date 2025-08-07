#! /usr/bin/python3
#Aqui va estar todo el codigo del programa 
import os
import getpass
from datetime import datetime
import json
from utils.colors import GREEN, RED, END, QST, FATAL #Se llama a las utilidades mas para decorar que funcionalidad

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
        dias_restantes = calcular_dias_restantes() #Aqui llamare a una funcion que se encarge de calcular los dias que faltan
        
        #Daremos diferentes prints dependiendo de cuantos dias faltan
        if dias_restantes >= 20:
            print(f"Quedan {dias_restantes} dias para tu cumpleaños {username}, ¡Se paciente!")
        elif dias_restantes < 10 and dias_restantes > 1:
            print(f"Quedan {dias_restantes} dias para tu cumpleaños ya no falta mucho {username}!")
        elif dias_restantes == 1:
            print(GREEN + "Mañana es tu cumpleaños!" + END + f"espero que tengas todo preparado para entonces {username}")
        elif dias_restantes == 0:
            print(GREEN + "FELIZ CUMPLEAÑOS" + END + f"{username} disfruta del dia!")
        elif dias_restantes == 359:
            print(f"Que tal te fue en tu cumpleaños de ayer {username}?")

def pedir_birth():
    # Aqui implementare la logica donde le pedire al usuario su fecha de cumpleaños
    while True:
        #Se le pide al usuario el birthday
        fecha = input(QST + " Introduce tu fecha de nacimiento DD/MM/YYYY (ejemplo: 31/12/2015): ") 
    
        try:
            #Comprobamos que la fecha este en el formato indicado
            birth = datetime.strptime(fecha, '%d/%m/%Y')
            if birth > datetime.today():
                print(FATAL+RED+"No puedes tener edad negativa o igual a 0\n"+END)
                continue
            else:
                confirm = input(QST+ f" Entonces la fecha es {fecha} correcto? (Y/N)") 
                
                if confirm == "y" or confirm == "Y":
                    return fecha
                else:
                    continue
        
        except ValueError:
            
            print(FATAL + " Formato no reconocido, por favor intentalo denuevo\n")


def create_json(): 
    #Esta funcion creara el json donde estara guardado el nombre y la fecha 
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
   

def calcular_dias_restantes():
    #calculamos los dias que faltan para el proximo cumpleaños
    username = getpass.getuser()
    archive_path = os.path.join(os.path.expanduser("~"), ".config", "hibirth", f"{username}_data.json")
    
    with open(archive_path, "r") as archive: #Abrimos el archivo
        datos = json.load(archive) #cargamos los datos en formato json

    fecha_str = datos["fecha"] #recordar que esta en STR y tiene que ser pasado a objeto de fecha

    fecha_nacimiento = datetime.strptime(fecha_str, '%d/%m/%Y') #Lo convertimos a un objeto
    
    #Ahora vamos a calcular cuanto falta para el proximo_cumple

    dia_cumple = fecha_nacimiento.day #Dia del cumpleaños
    mes_cumple = fecha_nacimiento.month #Mes del cumpleaños

    fecha_actual = datetime.today()
    year_actual = fecha_actual.year #año actual

    proximo_cumple = datetime(year_actual, mes_cumple, dia_cumple) #Configuramos la fecha del proximo cumpleaños

    #Vamos a hacer que si ya paso el cumpleaños de este año entonces lo pase al año siguiente
    
    if fecha_actual > proximo_cumple: #Si la fecha actual es un dato mayor que la fecha del cumpleaños de ese año
        proximo_cumple = datetime(year_actual +1, mes_cumple, dia_cumple) #Aumentamos 1 al año del proximo cumple

    dias_restantes = (proximo_cumple - fecha_actual).days
    
    return dias_restantes


#pedir_birth() #Con esto pruebo que la funcion pedir_birth este correcta
#create_json() #Probrar que la funcion funcione correectamente 
#first_init() #Probrar que la primera iniciacion funcione, este seria el main del programa

if __name__ == "__main__":
    try:    
        first_init() #Ejecutamos el script
    except KeyboardInterrupt:
        print("\n" + FATAL + RED + " Saliendo..." + END)
        exit(1)


