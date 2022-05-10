import types
types.MethodType(lambda self: None, None)

# tests for __subclasses__()

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(B):
    pass

class F(E):
    pass

class G(D, F):
    pass

print A.__subclasses__()
print B.__subclasses__()
print C.__subclasses__()
print D.__subclasses__()
print E.__subclasses__()
print F.__subclasses__()
print G.__subclasses__()

# test for __format__

print '{0:d}'.format(42)
print '{0:b}'.format(42)
print '{0:o}'.format(42)
print '{0:x}'.format(42)
print '{0:X}'.format(42)
print '{0:n}'.format(42)
print '{0:c}'.format
