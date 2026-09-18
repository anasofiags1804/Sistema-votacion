import json
from datetime import datetime

votos = {}
CANDIDATOS = ["Abelardo de la Espriella", "Gustavo Petro", "Alvaro Uribe", "Mafe Carrascal"]

def mostrar_candidatos():
    print("\nCandidatos disponibles:")
    for i, candidato in enumerate(CANDIDATOS, start=1):
        print(f"{i}. {candidato}")

def registrar_voto():
    persona = input("\nNombre de la persona que va a votar: ")
    if persona in votos:
        print(persona, "ya voto. No puede votar de nuevo.")
        return

    mostrar_candidatos()
    opcion = input("Elige el numero del candidato: ")

    if not opcion.isdigit() or not (1 <= int(opcion) <= len(CANDIDATOS)):
        print("Opcion invalida.")
        return

    candidato = CANDIDATOS[int(opcion) - 1]
    votos[persona] = candidato
    print("Voto registrado:", persona, "voto por", candidato)
    print("Voto registrado correctamente!")

def ver_resultados():
    if not votos:
        print("Aun no hay votos registrados.")
        return

    conteos = {candidato: 0 for candidato in CANDIDATOS}
    for candidato in votos.values():
        conteos[candidato] += 1

    total = len(votos)
    print("\nResultados de la votacion:")
    for candidato, cantidad in conteos.items():
        porcentaje = (cantidad / total) * 100 if total else 0
        print(f"{candidato}: {cantidad} votos ({porcentaje:.1f}%)")
    print(f"Total de votantes: {total}")

def guardar_historial():
    registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "votos": votos.copy()
    }

    try:
        with open("historial_votacion.json", "r") as archivo:
            historial = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []

    historial.append(registro)

    with open("historial_votacion.json", "w") as archivo:
        json.dump(historial, archivo, indent=4)

def reiniciar_votacion():
    if votos:
        guardar_historial()
        votos.clear()
        print("Votacion reiniciada. Los votos anteriores se guardaron en el historial.")
    else:
        print("No hay votos para reiniciar.")

def mostrar_menu():
    print("\n--- Sistema de Votacion ---")
    print("1. Votar")
    print("2. Ver resultados")
    print("3. Reiniciar votacion")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        registrar_voto()
    elif opcion == "2":
        ver_resultados()
    elif opcion == "3":
        reiniciar_votacion()
    elif opcion == "4":
        if votos:
            guardar_historial()
        print("Sistema finalizado.")
        break
    else:
        print("Opcion invalida.")
