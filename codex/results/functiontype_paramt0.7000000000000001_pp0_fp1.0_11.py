from types import FunctionType
list(FunctionType(lambda x:x**2,globals(),name='nome')(i) for i in range(5))

f=FunctionType(lambda x:x**2,globals(),name='nome')
f.__code__
dir(f)

#EXERCICIO 5
#Fibonacci
def fib(n):
    def fib0(n):
        if n == 0:
            return 0
        else:
            return 1
    def fib1(n):
        if n == 1:
            return 1
        else:
            return fib(n-1)+fib(n-2)
    if n == 0:
        return fib0(n)
    else:
        return fib1(n)

fib(5)

#EXERCICIO 6
#Fibonacci
def fib(n):
    def fib0(n):
        if n == 0:
            return 0
        else:
            return 1
    def fib1(n):
        if n == 1:
            return 1
        else:
            return fib(
