from types import FunctionType
a = (x for x in [1])
a.__name__

a = FunctionType(lambda x:x, globals())
a.__name__

a.name = 'a'
a.__name__

a.__qualname__

def a(): pass
a.__qualname__

def a(): pass
a.__qualname__

class A():
    def a(): pass
a = A()
A.a.__qualname__

class B(A):
    def a(): pass
B.a.__qualname__

class C(B):
    def a(): pass
C.a.__qualname__

class D(C):
    def a(): pass
D.a.__qualname__

class E(D):
    def a(): pass
E.a.__qualname__

class F(E):
    def a(): pass
F.a.__qualname__

class G(F):
    def a(): pass
G.a.__qualname__

class H(G):
    def a(): pass
H.a.__qualname__
