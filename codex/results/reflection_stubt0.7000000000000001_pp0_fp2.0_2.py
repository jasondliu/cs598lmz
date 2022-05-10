fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
code_obj = fn.__code__

class C:
    def meth(self): pass

class D(C):
    def meth(self): pass

class E(C):
    def meth(self): pass

class F:
    def meth(self): pass

class G(F):
    def meth(self): pass

class H(C, F):
    def meth(self): pass

# Test that the C3 MRO works as expected
assert(C.mro() == [C, object])
assert(D.mro() == [D, C, object])
assert(E.mro() == [E, C, object])
assert(F.mro() == [F, object])
assert(G.mro() == [G, F, object])
assert(H.mro() == [H, C, F, object])

# Test that __bases__ is correct
assert(C.__bases__ == (object,))
assert(D.__bases__ == (C,))
assert(E.__bases__
