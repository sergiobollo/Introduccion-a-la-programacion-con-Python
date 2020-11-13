#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      rubgonza
#
# Created:     15/10/2020
# Copyright:   (c) rubgonza 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import random

a = input("Introduce  1  para lanzar los dados")

a = 1
while a == 1:
    dado1 = random.choice([1,2,3,4,5,6])
    dado2 = random.choice([1,2,3,4,5,6])
    suma_dados = dado1+dado2
    print ("Has obtenido la siguiente tirada de dados:", dado1, "y", dado2)
    print ("El valor de la suma de tu tirada de dados es:", suma_dados)
    print ()
    a = input("Introduce  1  para volver a lanzar los dados. Introduce  0  para finalizar")
    a = int(a)
    continue
else:
    print ("Hasta pronto!")