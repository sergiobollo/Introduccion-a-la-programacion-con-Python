import random

def tirar_dados():
    tirar='si'
    while tirar=='si':
        valor_dado1=int(random.random()*10)%6+1
        valor_dado2=random.choice(range(1,7))
        suma_dados=valor_dado1+valor_dado2
        print('Dado 1:',valor_dado1)
        print('Dado 2:',valor_dado2)
        print('Total:',suma_dados)
        tirar=input("¿quiere tirar los dados otra vez? (si/no):")

tirar_dados()