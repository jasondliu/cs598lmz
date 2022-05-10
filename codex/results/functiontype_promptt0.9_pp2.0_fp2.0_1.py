import types
# Test types.FunctionType
class A:
    "New-style class"
    def foo(self, x):
        pass
    def bar(self, x, y, z=1):
        pass
    def f(self):
        return 1

def g1():
    "Function with no parameters"
    def baz(m, n):
        pass
    return baz
def g2(x):
    "Function with 1 parameter"
    def baz(m, n):
        pass
    return baz
def g3(x, y):
    "Function with 2 parameters"
    def baz(m, n):
        pass
    return baz

def f(foo, barcv):
    "Function with *args and **kwds parameters"
    def it():
        while 1:
            yield 1234
    try:
        foo(1, 2)
    except TypeError:
        pass
    if isinstance(barcv, types.FunctionType):
        print('barcv is a method')
    if isinstance(g2, types.FunctionType):
        print
