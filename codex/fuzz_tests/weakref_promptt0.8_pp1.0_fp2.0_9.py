import weakref
# Test weakref.ref in C code
import _weakref

# The list of weak reference objects to objects
refs = []

# The number of weakref callbacks.
CALLBACKS = 0

class C:
    pass

# Callbacks for weak reference objects
def callback(*args):
    global CALLBACKS
    CALLBACKS = CALLBACKS + 1

def typeerror(*args):
    raise TypeError

# Create a cycle and register some callback functions for the objects
# in the cycle.
c1 = C()
c2 = C()
refs.append(_weakref.create_weakref(c1, callback))
refs.append(_weakref.create_weakref(c2, typeerror))
refs.append(_weakref.create_weakref(c2, callback))
refs.append(_weakref.create_weakref(c1, typeerror))
c1.cycle = c2
c2.cycle = c1


def clear_all_weakrefs():
    for ref in refs[:]:
        del ref
    del refs[:]


