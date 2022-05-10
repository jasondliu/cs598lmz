import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo:
    def __init__(self):
        self.a = 1
    def __del__(self):
        print("Foo has been deleted")
    def __repr__(self):
        return "Foo"
f = Foo()
print(f)
f.b = Foo()
print(f)
w = weakref.ref(f)
print(w)
print(w())

del f.a
del f.b
print(w())
del f
print(w())

gc.collect()

print(w())
# weakref.ref()
import weakref
class Foo(object):
    def __init__(self):
        self.a = 1
    def __del__(self):
        print("Foo has been deleted")
    def __repr__(self):
        return "Foo"

f = Foo()
w = weakref.ref(f)
print(w())
del f
print(w())
print(w() is None)

class Node(object):
    def __init__(
