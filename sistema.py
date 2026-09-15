# sistema.py
votos = {}

def registrar_voto(persona, candidato):
    # Se revisa si la persona ya voto antes usando el diccionario
    if persona in votos:
        print(persona, "ya voto. No puede votar de nuevo.")
        return

    # Si no ha votado, se guarda el nuevo voto en el diccionario
    votos[persona] = candidato
    print("Voto registrado:", persona, "voto por", candidato)


while True:
    nombre = input("Nombre de la persona (o 'salir' para terminar): ")

    if nombre == "salir":
        break

    candidato = input("Por quien vota " + nombre + "?: ")
    registrar_voto(nombre, candidato)