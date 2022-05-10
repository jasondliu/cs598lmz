import weakref
# Test weakref.ref() with a cyclic gc.
import gc

# For making sure the refcounts are right during the tests
import sys

class TestCycle:
    def __init__(self, name):
        self.name = name
        self.cycle = self

    def __del__(self):
        print("calling TestCycle.__del__ for", self.name)

    def __repr__(self):
        return "<TestCycle %s>" % self.name

a = TestCycle("a")
b = TestCycle("b")
c = TestCycle("c")

# Create a bunch of cycles.
a.cycle = b
b.cycle = a

a.ref1 = weakref.ref(a)
ref2 = weakref.ref(a)
del a
del b
del c
gc.collect()
print("deleting ref2")
del ref2
gc.collect()

if verbose:
    print("CREATING cycles")

a = TestCycle("a")
wr = weakref.ref(a)


