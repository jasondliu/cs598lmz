import weakref
# Test weakref.ref with a metaclass.

# Weakrefs to classes should work:
class W:
    pass


wr = weakref.ref(W)
assert wr() is W

# Weakrefs to instances of classes with a metaclass should work:
class M(type):
    pass
class C(metaclass=M):
    pass


w = C()
wr = weakref.ref(w)
assert wr() is w
# Weakrefs to instances of classes with a metaclass should work:
class M(type):
    pass


class S(metaclass=M):
    pass


class C(S):
    pass


w = C()
wr = weakref.ref(w)
assert wr() is w
# Weakrefs to instances of classes with a metaclass should work:
class M(type):
    pass


class S(metaclass=M):
    pass


class C(S):
    pass


class D(C):
    pass


w = D()
wr = weakref.ref(w)
assert wr()
