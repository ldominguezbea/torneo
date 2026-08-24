from random import *
from tabulate import *
from colorama import init, Fore, Style


def crear_equipo():
    equipos = []
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
            equipos.append(equipo)
            cont +=1
        else:
            print("El equipo ya esta en la lista")
    return equipos

def estadisticas(local, visitante):

    global estadisticas
    gol_local = randint(0, 6)
    gol_visitante = randint(0, 6)

    local["PJ"] += 1
    visitante["PJ"] += 1

    local["GF"] += gol_local
    visitante["GF"] += gol_visitante

    local["GC"] += gol_visitante
    visitante["GC"] += gol_local

    local["DG"] = gol_local - gol_visitante
    visitante["DG"] = gol_visitante - gol_local

    if gol_local > gol_visitante:
        local["PTOS"] =+= 3
        local["PG"] += 1
        visitante["PP"] += 1
    elif gol_visitante > gol_local:
        visitante["PTOS"] += 3
        visitante["PG"] += 1
        local["PP"] += 1
    else:
        visitante["PTOS"] += 1
        local["PTOS"] = 1
        visitante["PE"] += 1
        local["PE"] = 1
    guardar(equipos)

def fixture(equipos):
    cant_equipos = len(equipos)
    for i in range():
        for x in range(i +1, cant_equipos):
            estadisticas(equipo[i], equipo[x])
    mostrar_fixture()
            
def mostrar_fixture():
    print(tabulate(estadisticas, headers = ["Nº de partido", 
    "Local", 
    "Goles", 
    "Puntos", 
    "Diferencia de puntos", 
    "Goles a favor", 
    "Goles en contra"
    "Visitante", 
    "Goles", 
    "Puntos", 
    "Diferencia de puntos", 
    "Goles a favor", 
    "Goles en contra"], tablefmt = "grid"))
    