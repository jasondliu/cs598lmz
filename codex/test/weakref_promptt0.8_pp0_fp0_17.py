import weakref
# Test weakref.ref
# Test weakref.proxy
import test.support
def ref(ob):
    return weakref.ref(ob)
def proxy(ob):
    return weakref.proxy(ob)
def proxy_factory(ob):
    return weakref.proxy(ob)
class C(object):
    def __init__(self, label):
        self.label = label
    def __repr__(self):
        return 'C(%s)' % self.label
class D(C):
    def __init__(self, label):
        super().__init__(label)
    def __repr__(self):
        return 'D(%s)' % self.label
class E(C):
    def __init__(self, label):
        super().__init__(label)
    def __repr__(self):
        return 'E(%s)' % self.label
def test():
    # Test basic behavior
    c = C('Hello')
    r = ref(c)
    p = proxy(r)
    assert r() is c
    assert p
