import weakref
# Test weakref.ref() == a.__weakref__

import gc
import weakref

class A:
    def __init__(self, name): self.name = name

    def __repr__(self):
        return "<A object %s>" % self.name

class WeakRef:
    def __init__(self, obj):
        self.wref = weakref.ref(obj)

    def __eq__(self, other):
        if isinstance(other, WeakRef):
            return other.wref == self.wref
        else:
            return other is self.wref()

    def __hash__(self):
        return hash(self.wref)

    def __repr__(self):
        return repr(self.wref)

# The A objects are kept alive by the list referenced by all_refs
all_refs = []

import string
# Make a bunch of A objects with reasonable refcounts
for i in range(100):
    for x in string.ascii_uppercase:
        name = "%i%s" % (
