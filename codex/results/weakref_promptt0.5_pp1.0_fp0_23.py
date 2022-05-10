import weakref
# Test weakref.ref() with a class that has a __del__ method.

class Foo:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "__del__ for", self.name

def callback(r):
    print "callback for", r()

f = Foo("f")
f_ref = weakref.ref(f, callback)
del f

print "gathering garbage..."
import gc
gc.collect()
