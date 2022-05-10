import weakref
# Test weakref.ref() to make sure it accepts an object and returns a
# weakref.ref object.

class Foo(object): pass

w = weakref.ref(Foo())
print(w)

# Now try it with an object that can't be weak referenced.

try:
    weakref.ref(1)
except TypeError:
    pass
else:
    print("Didn't raise TypeError")

# Now try it with an object that can't be weak referenced, but may
# be able to be weakly referenced.

try:
    weakref.ref(Foo)
except TypeError:
    pass
else:
    print("Didn't raise TypeError")
