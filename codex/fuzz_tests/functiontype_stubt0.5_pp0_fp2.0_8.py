from types import FunctionType
a = (x for x in [1])
type(a)

def f():
    pass

type(f)
type(f) == FunctionType

a = 1
type(a)
dir(a)
a.__add__(2)

def f():
    pass

type(f)
dir(f)
f.__call__()

a = 1
type(a)
dir(a)
a.__add__(2)

def f():
    pass

type(f)
dir(f)
f.__call__()

class A:
    pass

a = A()
type(a)
dir(a)
a.__call__()

class A:
    def __call__(self):
        print("A")

a = A()
type(a)
dir(a)
a.__call__()

a()

class A:
    def __call__(self, x):
        print(x)

a = A()
type(a)
dir(a)
a.__call__(2)

a
