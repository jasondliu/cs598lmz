import weakref
# Test weakref.ref() on built-in types.
import sys

class C:
    pass


class D(C):
    pass


class E:

    def __init__(self):
        self.foo = 1


class F(E):
    pass


class G:

    def __init__(self):
        self.foo = 1


class H(G):
    pass


class I(H):
    pass


d = D()
f = F()
h = H()
i = I()

for base in (object,):
    for target in (int, float, complex, str, bytes, tuple, list, dict, set, frozenset,
        C, D, E, F, G, H, I, type, object, object()):
        print(base, target)
        r = weakref.ref(target)
        p = weakref.proxy(target)
        t, w = type(r), type(p)
        if issubclass(type(target), C):
            assert t is weakref.ReferenceType
            assert w is weakref
