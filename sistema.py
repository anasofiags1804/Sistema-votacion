# sistema.py
votos = {}

def registrar_voto(persona, candidato):
    
    if persona in votos:
        print(persona, "ya voto. No puede votar de nuevo.")
        return


    votos[persona] = candidato
    print("Voto registrado:", persona, "voto por", candidato)


while True:
    nombre = input("Nombre de la persona (o 'salir' para terminar): ")

    if nombre == "salir":
        break

    candidato = input("Por quien vota " + nombre + "?: ")
    registrar_voto(nombre, candidato)