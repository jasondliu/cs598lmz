import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a bunch of objects, and make sure they get collected.
# The objects are not collectable until the weakrefs are dead.

import sys

def create(i):
    class C:
        def __init__(self):
            self.i = i
        def __repr__(self):
            return "<C %d>" % self.i
    return C()

# Create a bunch of objects, and make sure they get collected.
# The objects are not collectable until the weakrefs are dead.

# Create a bunch of objects, and make sure they get collected.
# The objects are not collectable until the weakrefs are dead.

def create(i):
    class C:
        def __init__(self):
            self.i = i
        def __repr__(self):
            return "<C %d>" % self.i
    return C()

# Create a bunch of objects, and make sure they get collected.
# The objects are not collectable until the weakrefs are dead.

def create(i):
    class C:
