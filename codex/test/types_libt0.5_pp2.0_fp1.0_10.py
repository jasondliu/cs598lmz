import types
types.MethodType(lambda self: None, None, D) # Type warning

def f(x):
    return x
D.method = f
D.method(d)

class C:
    def method(self):
        return self

c = C()
types.MethodType(lambda self: None, None, C) # Type warning

def f(x):
    return x
C.method = f
C.method(c)

class D(C):
    pass

d = D()
types.MethodType(lambda self: None, None, D) # Type warning

def f(x):
    return x
D.method = f
D.method(d)

class C:
    def method(self):
        return self

c = C()
