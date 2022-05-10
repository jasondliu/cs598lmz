from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f(x):
    return x
list(f.__code__)

# method objects
class C:
    def m(self, x):
        return x
list(C.m)

# built-in functions
list(abs)

# built-in methods
list(list.append)

# built-in types
list(int)

# classes
class C:
    pass
list(C)

# instances
class C:
    def __iter__(self):
        yield 1
        yield 2
        yield 3
list(C())

# generators
def g():
    yield 1
    yield 2
    yield 3
list(g())

# dictionary views
d = {'a': 1, 'b': 2, 'c': 3}
list(d.keys())
list(d.values())
list(d.items())

# custom objects
class C:
    def __iter__(self):
        yield 1
        yield 2
        yield 3
list
