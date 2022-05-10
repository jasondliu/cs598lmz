from types import FunctionType
a = (x for x in [1])
type(a)

for i in a:
    print(i)

b = a
b

c = b
c

d = c
d

def fun():
    print('this is a fun')

type(fun)

e = fun
e()

type(e)

def fun1(f):
    print(type(f))
    f()

fun1(fun)

# 闭包
def fun2(name):
    def fun3():
        print('hello', name)
    return fun3

a = fun2('nmsl')
a()

#闭包
def funx(x):
    def funy(y):
        return x * y
    return funy

a = funx(8)
print(a(5))

#闭包
def funm(m):
    def funn(n):
        return m + n
    return funn

a = funm(8)
print(a(5))

#闭包
def
