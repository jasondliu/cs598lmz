import weakref
# Test weakref.ref() can be chained.
class C(object):
    def __del__(self):
        pass

class D(object, C):
    pass

foo = D()
r = weakref.ref(foo)
wr = weakref.ref(r)
