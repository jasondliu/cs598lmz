import weakref
# Test weakref.reference with self-referencing objects.
import weakref

class X:

    def __init__(self):
        self.y = weakref.ref(self)

    def __del__(self):
        self.y()

x = X()
x.y()
# Test weakref callbacks.
import weakref

alive = []
dead = []

def callback(obj):
    dead.append(obj)

a = weakref.ref(alive, callback)
b = weakref.ref(dead, callback)
alive.append(a)
alive.append(b)
del dead[:]
del alive[:]
# Test weakref "constructor"
import weakref

def test_basic():
    def callback(o):
        return

    def create_obj():
        return object()

    obj = create_obj()
    ref = weakref.ref(obj, callback)
    assert ref() is obj
    assert ref() is not None
    del obj
    assert ref() is None
    assert (str(ref) == "dead weak
