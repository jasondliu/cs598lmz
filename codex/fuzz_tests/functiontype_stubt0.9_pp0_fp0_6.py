from types import FunctionType
a = (x for x in [1])
type(a)

#匿名函数
L = list(map(lambda x: x*x, [1,2,3,4,5]))
print(L)

#根据不同的条件指定不同的函数
def f(x):
    return x * x
def g(x):
    return x * x * x
def add(x,y,f):
    return f(x) + f(y)
a = add(-5,6,g)
print(a)

#编写高阶函数，就是让函数的参数能够接收别的函数
def add(x,y,f):
    return f(x) + f(y)
a = add(-5,6,abs)
print(a)

#map() 函数接收两个参数
