import weakref
# Test weakref.ref(a) == weakref.ref(b)

a = []
wr = weakref.ref(a)
b = []
wr2 = weakref.ref(b)
wr == wr2

import weakref

# This class is never instantiated, so '__call__' is
# never defined.
class Weak:
    pass

# Create a weakref to an object of this class
w = weakref.ref(Weak())

w() is None

import weakref

a = []
wr = weakref.ref(a)
wr() is a

# The original list is gone, so the weakref object has a bogus object
del a
wr() is None

import weakref
a = []

def callback(wr):
    print("object gone")

wr = weakref.ref(a, callback)
del a

import weakref

class MyClass:
    def my_method(self):
        pass

# Set up a weak reference to an instance
obj = MyClass()
r = weakref.ref(obj)

# Now create a
