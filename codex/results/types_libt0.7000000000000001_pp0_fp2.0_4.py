import types
types.MethodType(lambda self, x: x + 1, 
    type(1))(1)

a = type('a', (), {'x': 1, 'y': 2})
type(a)
type(a())


class A:
    def __init__(self, x):
        self.x = x

def f(self, y):
    return self.x + y

a = A(1)
a.f = types.MethodType(f, a)
a.f(2)


class A:
    def __init__(self):
        self.x = 1

def getx(self):
    return self.x

A.getx = getx
a = A()
a.getx()


class A:
    def __init__(self):
        self.x = 1
    def getx(self):
        return self.x

a = A()
a.getx()


class A:
    def __init__(self):
        self.x = 1
    def getx(self):
        return
