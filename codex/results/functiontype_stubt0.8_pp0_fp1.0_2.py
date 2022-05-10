from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
def f():
    a = 1
    yield
    a = 2

f().gi_yieldfrom

def g():
    a = 1
    yield from f()
    a = 2

g().gi_yieldfrom

def h():
    a = 1
    yield from (x for x in [1])
    a = 2

a().gi_yieldfrom

def i():
    a = 1
    yield from (x for x in [1])
    a = 2

b().gi_yieldfrom

class x:
    def __iter__(self):
        return iter([])

def j():
    a = 1
    yield from x()
    a = 2

j().gi_yieldfrom


class y:
    def __iter__(self):
        return iter([])

def k():
    a = 1
    yield from y()
    a = 2

k().gi_yieldfrom

class z(x, y): pass

def l():

