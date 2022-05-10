from types import FunctionType
a = (x for x in [1])
type(a)

def fun():
    a = 1
    b = 2
    return a, b

c = fun()
type(c)

b = fun
type(b)

print(isinstance(fun, FunctionType))
print(isinstance(fun, (FunctionType, int)))

def foo():
    pass
def bar():
    print('hello')
    pass
def foobar():
    return 'hello'

print(foo())
print(bar())
print(foobar())

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()
print(target)

register(target)
print(target)

def f1():
    print('f1')
def f2():
    print('f2')
def f3():
    print('f3')

register(f1)()
register(f2)()
register(f3)()

def f1():
    print('f1
