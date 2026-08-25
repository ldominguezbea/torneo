from random import randint
from tabulate import tabulate
from colorama import init, Fore
from archivos import guardar

init(autoreset=True)
def crear_equipo():
    dicc = []
    while True:
        try:
            cant = int(input("Ingrese la cantidad de equipos: "))
            break
        except ValueError:
            print("Error")
    cont = 0
    while cont != cant:
        equipo = input("Ingrese el nombre de su equipo:")
        if equipo not in [e["EQUIPO"] for e in dicc]:
            dicc.append({
                "EQUIPO": equipo, "PJ": 0, "PG": 0, "PE": 0, "PP": 0,
                "GF": 0, "GC": 0, "DG": 0, "PTS": 0,
            })
            cont += 1
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
    local["DG"] = local["GF"] - local["GC"]
    visitante["DG"] = visitante["GF"] - visitante["GC"]

    if gol_local > gol_visitante:
        local["PTS"] += 3
        local["PG"] += 1
        visitante["PP"] += 1
        print(local["EQUIPO"], Fore.GREEN + "ganó el partido")

    elif gol_visitante > gol_local:
        visitante["PTS"] += 3
        visitante["PG"] += 1
        local["PP"] += 1
        print(visitante["EQUIPO"], Fore.GREEN + "ganó el partido")
    else:
        local["PTS"] += 1
        visitante["PTS"] += 1
        local["PE"] += 1
        visitante["PE"] += 1
        print(Fore.YELLOW + "Empate")

def fixture(dicc):
    cant_equipos = len(dicc)
    for i in range(cant_equipos):
        for x in range(i + 1, cant_equipos):
            estadisticas(dicc[i], dicc[x])

    guardar(dicc, "equipos.json")
    campeon = dicc[0]
    for equipo in dicc:
        if equipo["PTS"] > campeon["PTS"]:
            campeon = equipo

    mostrar_fixture(dicc)
    print(Fore.CYAN + "Campeón:", campeon["EQUIPO"], "con", campeon["PTS"], "puntos")

def mostrar_fixture(dicc):
    filas = [[e["EQUIPO"], e["PJ"], e["PG"], e["PE"], e["PP"], e["GF"], e["GC"], e["DG"], e["PTS"]] for e in dicc]
    print(tabulate(filas, headers=["Equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "DG", "PTS"], tablefmt="grid"))