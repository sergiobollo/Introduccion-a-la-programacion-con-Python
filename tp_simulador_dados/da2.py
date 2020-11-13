import random
def dados():
    print("Â¡Bienvenido a los dados!") 
    a = random.randint(1,6)
    b = random.randint(1,6)
    print("Primer tirada: ", a, "Segunda tirada: ", b)
    print("La suma de sus puntos es", a, "+", b)
    c = a + b
    print("Su total es: ", c)
    respuesta = None
    while respuesta not in ("Y", "yes", "y", "N", "no", "n"):
        respuesta = input("Â¿Desea jugar otra vez? (Y/N) " )
        if respuesta[0] == "Y" or respuesta[0] == "yes" or respuesta[0] == "y":
            dados()
        elif respuesta[0] == "N" or respuesta [0] == "no" or respuesta == "n":
            exit
        else:
            print ("Respuesta invÃ¡lida")

dados()