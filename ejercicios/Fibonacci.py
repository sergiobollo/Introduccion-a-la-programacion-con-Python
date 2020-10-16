def fib(n):
	a,b=0,1
	c=0
	while c<n:
		a,b=b,a+b
		c=c+1
		print(a, end=" ")

fib(35)


def fib2(n):
	a,b=0,1
	for i in range(n):
		if i<n:
			i = i+1
			a,b=b,a+b
			print(a, end=" ")

fib2(35)