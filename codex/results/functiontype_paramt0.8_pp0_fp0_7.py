from types import FunctionType
list(FunctionType(f, globals(), 'foo', (int,), None))

class C:
    def g(self, x):
        pass

class D:
    pass

def h(x):
    pass

C.g(D(), h)

def f(x, y, z):
    return 1, 2, 3

list(f(1, 2, 3))

def f():
    raise Exception

def g():
    try:
        f()
        return 1
    except:
        return 2

print g()

def f(x, y):
    return x + (y * 10)

c = f(1, 2)

def f():
    return 1, 2, 3

def g(*args):
    print args

g(f())

def g(a, **b):
    print a
    print b

g(1, x = 2, y = 3)

def g(a, **b):
    return a, b

g(1, x = 2, y = 3)
a, b =
