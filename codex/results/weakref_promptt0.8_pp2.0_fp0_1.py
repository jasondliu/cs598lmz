import weakref
# Test weakref.ref() for various kinds of objects.

# Make a weakly referencable object:
class C:
    pass

c = C()
c.attr = C()

# Reference it from various kinds of objects:
r0 = weakref.ref(c)
r1 = weakref.ref(c.attr)
r2 = weakref.ref(c, lambda u: None)
r3 = weakref.ref(c.attr, lambda u: None)
r4 = weakref.ref(C)
r5 = weakref.ref(C.__dict__['__repr__'])

# Check they can all be called:
r0()
r1()
r2()
r3()
r4
r5

# Check they are really weak references:
del c
del c.attr
try:
    r0()
except ReferenceError:
    pass
else:
    print("ReferenceError should be raised")

try:
    r1()
except ReferenceError:
    pass
else:
    print("ReferenceError should be raised")

# Check they can
