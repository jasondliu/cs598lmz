import weakref
# Test weakref.ref(subclass)
class A(object): pass
class B(A): pass
class C(B): pass
class D(C): pass

def test():
    b = B()
    c = C()
    d = D()
    a = A()
    wr = weakref.ref(a)
    assert wr().__class__ is A

    wr = weakref.ref(b)
    assert wr().__class__ is B

    wr = weakref.ref(c)
    assert wr().__class__ is C

    wr = weakref.ref(d)
    assert wr().__class__ is D

test()
