from types import FunctionType
a = (x for x in [1])
type(a)

type(abs)
type(lambda x: x)
type(x for x in [1])

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

type(fact)

fact(10)

fact(10)

fact(1)

fact(2)

fact(1)

fact(0)

fact(-1)

fact(5)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact(5)

fact_iter(5,1)

fact_iter(4,5)

fact_iter(3,20)

fact_iter(2,60)

fact_iter(1,120)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if
