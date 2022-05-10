import weakref
# Test weakref.ref()
import types

class A:
    def meth(self):
        pass

class B(A):
    pass

class C(object):
    pass

for proto in [A, B, C]:
    inst = proto()
    r = weakref.ref(inst)
    assert r() is inst
    r = weakref.ref(inst, lambda x: None)
    assert r() is inst
    assert r.__call__() is inst
    assert r.__hash__()
    assert r.__call__().__hash__()
    assert r.__hash__() == r.__call__().__hash__()
    assert r.__str__()
    assert r.__call__().__str__()
    assert r.__str__() == r.__call__().__str__()
    assert r.__repr__()
    assert r.__call__().__repr__()
    assert r.__repr__() == r.__call__().__repr__()
