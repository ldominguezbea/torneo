import json
def guardar(dicc, archivo =" equipos.json"):
    with open(archivo, "w", encoding = "utf-8") as f:
        json.dump(dicc, f, ensure_ascii = False, indent = 4)   
