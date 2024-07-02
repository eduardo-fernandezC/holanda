import os
os .system("cls")


import random

def run():
    score_player = 0
    score_computer = 0

    for i in range(5):
        print(f"Turno {i+1}")
        print("Elige una opción de disparo:")
        print("1. Angulo izquierdo")
        print("2. Centro")
        print("3. Angulo derecho")
        print("4. Aleatorio")
        print("5. Potente")
        option = int(input("Ingrese su opción: "))

        if option == 1:
            score_player_turn = random.randint(1, 5)
        elif option == 2:
            score_player_turn = random.randint(6, 10)
        elif option == 3:
            score_player_turn = random.randint(11, 15)
        elif option == 4:
            score_player_turn = random.randint(1, 15)
        elif option == 5:
            score_player_turn = random.randint(16, 20)
        else:
            print("Opción inválida. Seleccionando una opción aleatoria.")
            score_player_turn = random.randint(1, 15)

        score_computer_turn = random.randint(1, 15)

        if score_player_turn > score_computer_turn:
            print("¡Gol del jugador!")
            score_player += 1
        elif score_player_turn < score_computer_turn:
            print("¡Gol del computador!")
            score_computer += 1
        else:
            print("¡Empate!")

    print(f"El jugador anotó {score_player} goles y el computador anotó {score_computer} goles.")
    if score_player > score_computer:
        print("¡El jugador gana el partido!")
    elif score_player < score_computer:
        print("¡El computador gana el partido!")
    else:
        print("¡El partido terminó en empate!")

if __name__=="__main__":
    run()