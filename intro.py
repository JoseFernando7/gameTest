from utilities import clear, verifyInput
import Chapter1
import sys


def presentation():
    clear()
    print("""Vives en Bogotá, el día de hoy saliste más tarde de lo normal de tu trabajo y tienes que ir hasta tu casa 
al otro lado de la ciudad. Recorrer todo Bogotá a las 9:30 de la noche solo parece una tarea complicada pero no te 
preocupes, si eres inteligente puedes lograr llegar a salvo a la estación de metro que te garantiza llegar a salvo a tu 
casa pero para eso debes evadir todos los peligros que te puedas encontrar ¿Comenzamos?
(Escribe el número (sin espacios) correspondiente a la acción que deseas realizar y luego pulsa enter para continuar)

[1] De una
[2] No, a la verga
""")

    option = input(" >_ ")
    num = verifyInput(option)

    if num and option == '1':
        clear()
        Chapter1.scene1()
    elif num and option == '2':
        clear()
        print("Ahhhhhhhhhh mucha loca")
        input("")
        sys.exit()
    else:
        clear()
        print("Esa ni siquiera es una opcion, SUBNORMAL")
        input("")
        presentation()
