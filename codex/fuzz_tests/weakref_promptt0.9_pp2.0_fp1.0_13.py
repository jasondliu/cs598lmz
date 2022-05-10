import weakref
# Test weakref.ref
import weakref

class Foo:
    def __init__(self):
        self.x = 1 

f = Foo()
x = weakref.ref(f)
assert x() is f
f = None   # f is being destroyed
assert x() is None
# Test weakref.finalize
import weakref
class Foo:
    def __init__(self):
        self.x = 1 

l = []

def callback(ref):
    l.append(ref.x)

def add_finalizer(obj):
    ref = weakref.finalize(obj, callback)
    return ref

f = Foo()
add_finalizer(f)
assert len(l) == 0
del f
assert len(l) == 1
assert l[0] == 1 
# Test weakref.proxy
import weakref
class Foo:
    def __init__(self):
        self.x = 1 

f = Foo()
p = weakref.proxy(f)
assert p.x == 1
# test weakref.WeakSet
import weak
