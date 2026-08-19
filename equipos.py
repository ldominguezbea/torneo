from random import *
from tabulate import *

equipos = []

def crear_equipo():
    global equipos
    lista = []
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

def partido():
    rojo = "\033[91m"
    verde = "\033[92m"
    amarillo = "\033[93m"
    celeste = "\033[96m"
    fin = "\033[0m"

    partidos = []
    num = 0
    for equipo in equipos:
        random1 = choice(equipos)
        random2 = choice(equipos)
        gol1 = randint(0, 6)
        gol2 = randint(0, 6)
        punt1 = 0
        punt2 = 0

        if gol1 > gol2:
            gol1 = verde + gol1 + fin
            gol2 = rojo + gol2 + fin
            punt1 = 3
            punt2 = 0
        elif gol1 < gol2:
            gol2 = verde + gol2 + fin
            gol1 = rojo + gol1 + fin
            punt1 = 0
            punt2 = 3
        else:
            gol2 = amarillo + gol2 + fin
            gol1 = amarillo + gol1 + fin
            punt1 = 0
            punt2 = 0
        num += 1

        for 0, 1, 2, 3, 4. 5, 6, 7 in partidos:



        while random1 == random2:
            random2 = choice(equipos)

        tupla = tuple()
        tupla = (num, ",", random1, ",", gol1, ",", random2, ",", gol2)

        partidos.append(tupla)

    print(tabulate(partidos, headers = ["Nº de partido", "Local", "Goles", "Visitante", "Goles", "Puntos", "Diferencia de puntos", "Goles a favor", "Puntos"], tablefmt = "grid"))



    
             