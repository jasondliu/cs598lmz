import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.ref(obj, callback, key)

# Test weakref.proxy(obj)
# Test weakref.proxy(obj, callback)

class Foo(object):
    x = 0
    def __init__(self, x):
        self.x = x
