from utilities import clear, gameOver, verifyInput

# Finales capitulo 1:
# final_1 = False Carlos hdp
# final_2 = False Carnicería "El Porcino Feliz"


def scene1():
    clear()
    print("""Recordemos: son las 9:30pm y tu meta es llegar a la estación de metro antes de que parta el último 
transporte a las 11pm.
Sales de tu oficina, como esperabas, no hay nadie en la calle. Carlos, tu compañero del trabajo, te dice que lo esperes
hasta que termine de darle al Excel aunque no sabes a que horas termina, recuerda que debes llegar a la estación antes
de las 11pm
¿Qué haces?

[1] Irte y empezar tu recorrido hacia la estación
[2] Esperar a Carlos
""")

    option = input(" >_ ")
    num = verifyInput(option)

    if num and option == '1':
        clear()
        scene2()
    elif num and option == '2':
        clear()
        print("""Decides esperar a Carlos a que termine con el Excel, pero cuando termina son las 12:15am, demasiado 
tarde para ir a la estación de metro. Alguien llega en moto a recojer a Carlos, le dices que te lleve pero no lo hace
y se marcha a su casa con la otra persona, dejándote tirado en la entrada de tu trabajo.
Le gritas 'gonorrea' a Carlos mientras lo ves alejándose, te quedas derrotado y perdido.
""")

        final = 1
        gameOver(final)
    else:
        clear()
        print("Esa ni siquiera es una opcion, SUBNORMAL")
        input("")
        scene1()


def scene2():
    clear()
    print("""Empiezas tu travesía hacia la estación de metro. Te topas con una calle que está cerrada debido a 
construcciones, más allá de la calle se encuentra un parque que está camino a la estación. 
Tienes dos direcciones: por la izquierda está el camino más corto, pero no es nada confiable lo que te puedas encontrar
ahí; hacia la derecha el camino es más largo, se supone es más seguro pero, aún así, cualquier cosa puede pasar allí.
¿Qué haces?

[1] Te vas por el camino de la izquierda.
[2] Te vas por el camino de la derecha.
[3] Que te valga verga todo y atravezar la calle que está en obras.
""")

    option = input(" >_ ")
    num = verifyInput(option)

    if num and option == '1':
        clear()
        scene2_1()
    elif num and option == '2':
        clear()
        scene2_2()
    elif num and option == '3':
        clear()
        print("""¿De verdad? Ok... Decides utilizar la que parece ser tu única neurona y te adentras en la obra de la 
calle que tienes en frente, obviamente, hay muchos huecos y maquinaria de construcción; como tampoco hay luz está todo 
oscuro por lo que caes en un hueco lastimándote la pierna izquierda al punto de que comienzas a sangrar, aún así no 
parece ser mucho problema para tí por el momento y logras atravezar la obra de la calle. 

Logras volver al camino principal pero tienes una herida evidente...""")
        input("")
        scene3()
    else:
        clear()
        print("Esa ni siquiera es una opcion, SUBNORMAL")
        input("")
        scene2()


def scene2_1():
    clear()
    print("""Te metes por el camino de la izquierda, avanzas un par de cuadras cuando llegas a una especie de carnicería
en donde hay dos personas encapuchadas las cuales, al acercarte, te preguntan si tienes carne; como les respondes 
que no, te preguntan si quieres un poco de carne y recuerdas que tienes un poco de hambre por el duro día de trabajo. 
¿Qué haces?

[1] Decirles que si.
[2] Ignorarlos y seguir tu camino.
[3] Volver sobre tus pasos hasta el lugar en el que te desvíaste.
""")

    option = input(" >_ ")
    num = verifyInput(option)

    if num and option == '1':
        clear()
        print("""Como tienes mucha hambre les dices que si por lo que ellos te piden que entres en la carnicería para
dártela. Cuando entras te das cuenta que es una carnicería ilegal que vende carne humana y que van a surtir las vitrinas
del día siguiente contigo. Las personas te matan, te descuartizan y, al día siguiente, la libra de tu carne a 5.000 
pesos se vende como pan caliente
""")

        final = 2
        gameOver(final)

    elif num and option == '2':
        clear()
        print("""Decides ignorar a las personas y sigues tu camino. 
Logras volver al camino principal pero te quedas con un sentimiento de incomodidad...""")
        input("")
        scene3()
    elif num and option == '3':
        clear()
        print("Te llenas de miedo y regresas hasta el punto en el que te desviaste...")
        input("")
        scene2()
    else:
        clear()
        print("Esa ni siquiera es una opcion, SUBNORMAL")
        input("")
        scene2_1()


def scene2_2():
    clear()
    print("""Vas por el camino de la derecha, todo parece ir bien hasta que te encuentras a una persona que está 
paseando a su perro, notas que tiene bozal y decides acercarte a saludar y acariciar a su perro. De repente el perro
empieza a verte mal porque hueles a pendejo; el perro se enoja contigo, tanto que se libera de su correa, también de su 
bozal y comienza a perseguirte queriendo morderte y sales corriendo.
¿Qué haces?

[1] Correr lo más que puedas, hasta donde te dé el aliento.
[2] Subir a un árbol.
""")

    option = input(" >_ ")
    num = verifyInput(option)

    if num and option == '1':
        clear()
        print("""'Piernas, para que las quiero' Es lo que dices antes de salir corriendo como cuando se van a acabar
las empanadas en la fritanga de la esquina. No volteas a mirar hacia atrás pues lo único que te interesa ahora es 
escapar. Después de un momento corriendo a todo lo que das te detienes y observas que el perro ya no te persigue por lo
que te tranquilizas.

Logras volver al camino principal con cierta preocupación sobre ese perro...""")
        input("")
        scene3()
    elif num and option == '2':
        clear()
        print("""Te subes al primer árbol que encuentras con la esperanza de evitar al perro que te persigue. Te toca 
esperar ahí un momento hasta que llega el dueño y tranquiliza al perro, llevándoselo consigo y pidiéndote disculpas 
en el proceso. 

Logras volver al camino principal...""")
        input("")
        scene3()
    else:
        clear()
        print("Esa ni siquiera es una opcion, SUBNORMAL")
        input("")
        scene2_2()


def scene3():
    clear()
    print("Hola, soy la escena 3")
