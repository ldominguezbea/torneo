from random import *
from tabulate import *

equipos = []

def crear_equipo():
    lista = []
    equipos = {}
    cont = 0
    cant = 0

    while True:
        try:
            cant = int(input("Ingrese la cantidad de equipos: "))
            break
        except ValueError:
            print("Error")
        
    while cont != cant:
        equipo = input("Ingrese el nombre de su equipo:")
        if equipo not in equipos:
            equipos[equipo] = {"PJ":0, "G":0, "P": 0, "E":0, "GA":0,"GC": 0, "PTOS":0}
            cont +=1
        else:
            print("El equipo ya esta en la lista")
def armar_fixture(equipos):
    fixture = {}
    for i in range((len(equipos) + 2) * 2):
        fixture[f"fecha {i}"] = {}

def partido():
    rojo = "\033[91m"
    verde = "\033[92m"
    amarillo = "\033[93m"
    celeste = "\033[96m"
    fin = "\033[0m"

    print(tabulate(partidos, headers = ["Nº de partido", "Local", "Goles", "Puntos", "Visitante", "Goles", 
                                        "Puntos", "Diferencia de puntos", "Goles a favor", 
                                        "Goles en contra"], tablefmt = "grid"))



    
             