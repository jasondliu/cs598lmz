import weakref
# Test weakref.ref(subclass(A))
class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
for base1 in A, B, C, D:
    for base2 in A, B, C, D:
        if issubclass(base1, base2):
            assert weakref.ref(base1())() is not None
        else:
            assert weakref.ref(base1())() is None


class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
for base1 in A, B, C, D:
    for base2 in A, B, C, D:
        if issubclass(base1, base2):
            assert weakref.ref(base1)() is not None
        else:
            assert weakref.ref(base1)() is None

class A(object):
    pass
class B(A):
    pass
class C(A):

