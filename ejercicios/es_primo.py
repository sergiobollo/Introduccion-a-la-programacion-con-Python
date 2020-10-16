def es_primo(numero):
       resultado = True
       c=0
       for divisor in range(2, numero):
           c+=1
           print(c)
           if (numero % divisor) == 0:
                resultado = False
                break
                print(c)
                return resultado

es_primo(13)