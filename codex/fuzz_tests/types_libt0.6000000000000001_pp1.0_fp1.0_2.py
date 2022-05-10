import types
types.MethodType(repr, object)

print(repr(object()))

object.__repr__ = lambda self: 'hello'
print(repr(object()))

class A: pass
class B(A): pass
print(A.__repr__(A()))
print(B.__repr__(B()))

class C(A):
    def __repr__(self):
        return 'world'

print(C.__repr__(C()))

class D(A):
    def __repr__(self):
        return super().__repr__()

print(D.__repr__(D()))

class E(A):
    def __repr__(self):
        return super(A, self).__repr__()

print(E.__repr__(E()))

class F(A):
    def __repr__(self):
        return super(F, self).__repr__()

print(F.__repr__(F()))

class G(A
