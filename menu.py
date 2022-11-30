import threading
from TrendUpdate import *
from trendGraphDetection import *



if __name__ == "__main__":
    print(f'Sistema de Administraciòn de Red'.center(50, "-"))
    print(f'Practica 3 -Monitoreo'.center(50, "-"))
    print(f''.center(50, "-"))
    print("Opciones: ")
    print("1: Iniciar")
    print("2: Salir")

    opc = int(input("Ingresa la opciòn: "))

    if opc == 1:
        print("Monitoreo de la RAM, CPU, RED del agente...")
        comunidad = input("Ingresa la comunidad: ")
        print(f'Puerto: 161')
        host = input("Ingresa el Host/IP: ")
        hilo =threading.Thread(target=actualizar_todo,args=(comunidad,host))
        hilo2 =threading.Thread(target=graficar_todo,args=())

        print("Iniciando el monitoreo.....")
        hilo.start()
        hilo2.start()
    elif opc == 2:
        quit()
    else:
        print(f'La opciòn {opc} no es correcta, seleccione de nuevo.')
        quit()