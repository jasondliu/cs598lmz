from types import FunctionType
a = (x for x in [1])
a

next(a)

def f():
    yield 1

f

next(f())

def g(x):
    yield x

next(g(1))

def h(x):
    return x

h

h(1)

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f'A({self.x})'

a = A(1)

a

a.x

a.x = 2

a

a.y = 1

a.y

a.z

a.z = 1

a.z

a.__dict__

a.__slots__ = ['x', 'y']

a.z = 1

a.__dict__

a.z

a.x = 1

a.y = 2

a.__dict__

a.__slots__ = ['x']

a.y

a.y = 2

a.
