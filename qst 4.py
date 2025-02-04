import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativa = None

    print("Tente adivinhar o número entre 1 e 100!")

    while tentativa != numero_secreto:
        tentativa = int(input("Digite seu palpite: "))

        if tentativa < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif tentativa > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print("Parabéns! Você acertou o número!")



jogo_adivinhacao()
