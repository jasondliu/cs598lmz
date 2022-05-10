import weakref
# Test weakref.ref as a function

class KeyDictionary:
    def __init__(self):
        self.d = {}
    def __getitem__(self, item):
        if item not in self.d:
            self.d[item] = 0
        self.d[item] += 1
        return self.d[item]
    def __delitem__(self, item):
        del self.d[item]
    def __len__(self):
        return len(self.d)

class Object(KeyDictionary):
    pass

class A(Object):
    pass

class B(Object):
    pass

class C(A, B):
    pass

def test_weakref_init():
    o = Object()
    assert o[3] == 1
    r = weakref.ref(o)
    assert r() is o
    assert o._refcount == 1

def test_weakref_call():
    o = Object()
    assert o[3] == 1
    r = weakref.ref(o)
    assert r() is o
