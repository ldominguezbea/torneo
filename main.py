from colorama import Fore
from equipos import (cargar_equipos, crear_tabla_inicial, simular_partido,actualizar_estadisticas,ordenar_posiciones,mostrar_tabla_final,)
def main():
    print("===TORNEO===")
    nombres = cargar_equipos()
    equipos = crear_tabla_inicial(nombres)
    for i in range(len(equipos)):
        for j in range(i + 1, len(equipos)):
            gol_local, gol_visitante = simular_partido(equipos[i], equipos[j])
            actualizar_estadisticas(equipos[i], equipos[j], gol_local, gol_visitante)
    equipos = ordenar_posiciones(equipos)
    mostrar_tabla_final(equipos)
    campeon = equipos[0]
    print(Fore.CYAN + f"Campeón: {campeon['EQUIPO']} con {campeon['PTS']} puntos")
main()