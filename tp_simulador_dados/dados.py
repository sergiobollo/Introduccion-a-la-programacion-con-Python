# Crear un programa que simule la tirada de dados.
# Cada vez que ejecutamos el programa, éste elegirá dos números aleatorios entre el 1 y el 6. 
# El programa deberá imprimirlos en pantalla, imprimir su suma y preguntarle al usuario si quiere tirar los dados otra vez.
# Autor: Roberto Guerrero Z.
# Fecha; 16-10-2020

import random

while True:
    tirar_dados = input("¿Deseas tirar los dados? S/N :")
    if tirar_dados in ("S", "s"):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print("Has tirado los dados\n Primer dado: ", dado1, "\n Segundo dado:", dado2) 
        print("Los dados suman:", dado1 + dado2, "\n")
    elif tirar_dados in ("N", "n"):
        break
    else:
        print("Por favor ingresa una respuesta válida 'S','s','N','n'")
print("¡Hasta pronto!")

