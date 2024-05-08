import random

def jugar_piedra_papel_tijeras():
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    while True:
        # Imprime las opciones y solicita la elección del usuario
        print("Elige una opción: piedra, papel o tijeras")
        opcion_usuario = input().lower()

        # Genera la opción aleatoria de la computadora
        opciones = ["piedra", "papel", "tijeras"]
        opcion_computadora = random.choice(opciones)

        # Imprime la elección de la computadora
        print("La computadora elige:", opcion_computadora)

        # Comprueba quién gana
        if opcion_usuario == opcion_computadora:
            print("¡Empate!")
        elif (opcion_usuario == "piedra" and opcion_computadora == "tijeras") or \
             (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
             (opcion_usuario == "tijeras" and opcion_computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

        # Pregunta al jugador si quiere jugar de nuevo
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_de_nuevo != "si":
            print("¡Gracias por jugar! ¡Hasta luego!")
            break

jugar_piedra_papel_tijeras()


