import json
def guardar(equipos, archivo = equipos.json):
    with open(equipos, "w", encoding = "utf-8") as f:
        json.dump(equips, f, ensure_ascii = False, indent = 4)   
