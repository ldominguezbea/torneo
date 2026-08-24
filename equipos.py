from random import *
from tabulate import *
from colorama import init, Fore, Style

init (autoreset = True)
def crear_equipo(): 
    dicc = {}
    global dicc 
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
        if equipo not in dicc:
            dicc.append(
                {
                "equipo": equipo,
                "pj": 0,
                "pg": 0,
                "pe": 0,
                "pp": 0,
                "gf": 0,
                "gc": 0,
                "dg": 0,
                "pts": 0,
            }
        )
            cont +=1
        else:
            print("El equipo ya esta en la lista")
    return dicc

def estadisticas(local, visitante):

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
        print(local, Fore.GREEN +"ganó el partido")
        visitante["PP"] += 1
    elif gol_visitante > gol_local:
        visitante["PTOS"] += 3
        visitante["PG"] += 1
        local["PP"] += 1
        print(visitante, Fore.GREEN + "ganó el partido")
    else:
        visitante["PTOS"] += 1
        local["PTOS"] = 1
        visitante["PE"] += 1
        local["PE"] = 1
        print(Fore.YELLOW + "Empate")
    guardar(equipos)

def fixture(equipos):
    campeon =  {
                "EQUIPO": equipo,
                "PJ": 0,
                "PG": 0,
                "PE": 0,
                "PP": 0,
                "GF": 0,
                "GC": 0,
                "DG": 0,
                "PTS": 0,
            }
        )
    cant_equipos = len(equipos)
    for i in range():
        for x in range(i +1, cant_equipos):
            estadisticas(equipo[i], equipo[x])
    for clave, valor in dicc.items():
        if dicc[clave]["PJ"]["PG"] > campeon["EQUIPO"]["PJ"]["PG"]:
            campeon[clave]

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
    