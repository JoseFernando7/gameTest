# Cosas
import os
import sys


def clear():
    os.system("cls||clear")


def gameOver(final):
    print("Has perdido")

    if final == 1:
        print("Final 1 de ??: Carlos hdp")
    elif final == 2:
        print('Final 2 de ??: Carnicería "El Porcino Feliz" ')

    input("")
    sys.exit()


def verifyInput(option):
    try:
        int(option)
        return True
    except ValueError:
        return False
