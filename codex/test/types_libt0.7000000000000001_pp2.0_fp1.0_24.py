import types
types.ModuleType('m')

class A:
    pass

def f():
    return 1

def g():
    return 2

def h(x):
    return 3

def i(x: A):
    return 4

def j(x: 'A'):
    return 5

def k(x: 'A', y: A):
    return 6

def l(x, y=2):
    return 7

def m(x, *args):
    return 8

def n(x, **kwargs):
    return 9

class B:
    def f(self):
        return 1
    def g(self):
        return 2
    def h(self, x):
        return 3
    def i(self, x: A):
        return 4
    def j(self, x: 'A'):
        return 5
    def k(self, x: 'A', y: A):
        return 6
    def l(self, x, y=2):
        return 7
