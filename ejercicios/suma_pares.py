def suma_pares(n):
    sum=0
    i=0
    while i <=n:
        if(i%2==0):
            sum= sum + i
        i=i+1
    print(sum)

suma_pares(100)