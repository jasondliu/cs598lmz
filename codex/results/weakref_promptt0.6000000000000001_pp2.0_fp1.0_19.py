import weakref
# Test weakref.ref(f) with a callable object
class C(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, *args):
        return self.name, args

def f(obj):
    print "calling f with", obj
    return obj

def callback(obj):
    print "callback called with", obj

c = C("function")
r = weakref.ref(f, callback)
print "f is", f
print "c is", c
print "r is", r
print "r() is", r()
print "deleting f"
del f
print "r() is", r()
print "c() is", c()
