# sistema.py
import json
from datetime import datetime

votos = {}

def registrar_voto(persona, candidato):
    # Se revisa si la persona ya voto antes usando el diccionario
    if persona in votos:
        print(persona, "ya voto. No puede votar de nuevo.")
        return

    # Si no ha votado, se guarda el nuevo voto en el diccionario
    votos[persona] = candidato
    print("Voto registrado:", persona, "voto por", candidato)

def ver_resultados():
    if not votos:
        print("Aun no hay votos registrados.")
        return
    
    conteos = {}
    for candidato in votos.values():
        conteos[candidato] = conteos.get(candidato, 0) + 1

    total = len(votos)
    print("\nResultados de la votación:")
    for candidato, cantidad in conteos.items():
        porcentaje = (cantidad / total) * 100
        print(f"{candidato}: {cantidad} votos ({porcentaje:.1f}%)")
    print(f"Total de votantes: {total}")

def reiniciar_votacion():
    if votos:
        guardar_historial()
        votos.clear()
        print("Votación reiniciada. Todos los votos anteriores han sido guardados en el historial.")
    else:
        print("No hay votos para reiniciar.")


def guardar_historial():
    registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "votos": votos.copy()
    }

    try:
        with open("historial_votacion.json", "r") as archivo:
            json.dump(registro, archivo)
            historial = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []

    historial.append(registro)

    with open("historial_votacion.json", "w") as archivo:
        json.dump(historial, archivo, indent=4)


while True:
    nombre = input("Nombre de la persona (o 'salir' para terminar): ")

    if nombre == "salir":
        break

    if nombre == "resultados":
        ver_resultados()
        continue

    if nombre == "reiniciar":
        reiniciar_votacion()
        continue
    
    candidato = input("Por quien vota " + nombre + "?: ")
    registrar_voto(nombre, candidato)

