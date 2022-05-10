import weakref
# Test weakref.ref(1)

import gc
import weakref

class Foo:
    pass

foo = Foo()

# Create a weak reference to foo.
foo_ref = weakref.ref(foo)

# Delete foo from the namespace.
del foo

gc.collect()

print(foo_ref())

# Create a dictionary that maps foo to 'bar'.
d = {foo_ref(): 'bar'}

print(d)

# Delete foo from the namespace.
del foo_ref

gc.collect()

print(d)

# Create a new Foo object.
foo = Foo()

# This will throw a KeyError, because the weak reference to the old
# foo object has been cleared by the garbage collector.
print(d[foo])

# Test weakref.proxy(1)

import weakref
import sys

class ExpensiveObject:
    def __del__(self):
        print('(Deleting %s)' % self)

obj = ExpensiveObject()
r = weakref.ref(obj)
