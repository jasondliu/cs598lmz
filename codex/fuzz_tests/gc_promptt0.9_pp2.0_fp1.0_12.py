import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect recursive behavior with a
# chain of weakrefs back to self
d = {}
for i in range(5):
    d[i] = weakref.ref(d)
print(d)
d[0]()
# Circular self-referential object with a __del__ method
class A:
    def __init__(self, v=None):
        self.v = v
    def __del__(self):
        print("A: self:", self, " v:", self.v)
        del self.v
#A(1)
#A(A(1))
a = A(123)
a = None
#A(a)
#a
# Test weakref.ref's ability to call a bound method as a callback
class Foo:
    def __init__(self, callback, v=None):
        self.v = v
        def weak_cb(w, selfref=ref(self)):
            # 'self' may have been destroyed before the callback is invoked
            self = selfref()
            if self is not None:
                callback(self)

