#Aqui va estar todo el codigo del programa 

from datetime import datetime

#Esta funcion solo sera llamada si es que el usuario habre por primera ves el programa
#o por si no hay un archivo de configuracion donde esten alojados los datos

def pedir_birth():
    # Aqui implementare la logica donde le pedire al usuario su fecha de cumpleaños
    while True:
        fecha = input("Introduce tu fecha de nacimiento DD/MM/YY (ejemplo: 31/12/2015): ")
        try:
            datetime.strptime(fecha, '%d/%m/%Y')
            break
        except ValueError:
            print("Formato no reconocido, por favor intentalo denuevo")

pedir_birth() #Con esto pruebo que la funcion este correcta
