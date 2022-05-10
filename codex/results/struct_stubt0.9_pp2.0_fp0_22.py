from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__

s = object()
s.a = 1
hasattr(s, 'a')
s.a
s.__dict__
s.b = 2
s.__dict__
s.__dict__ = {'b': 2}

class S:
    pass

s = S()
s.a = 1
s.a
s.__dict__
del s.a
s.a
s.__dict__

class S:
    pass

s = S()
s.a = 1
s.__dict__
S.a
del S.a
s.a
s.__dict__

class A:
    def f(self):
        return 42
    def g(self):
        return 3

a = A()
a.f(), a.g()
dir(a)
dir(A)
type(A)
type(A.f)
A.f.__class__

type.__dict__
callable(type)
callable(A)
callable(A.f)
