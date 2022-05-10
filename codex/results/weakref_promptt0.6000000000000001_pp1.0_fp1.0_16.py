import weakref
# Test weakref.ref() and weakref.proxy() with a variety of argument types.
# Also test gc.get_referrers().

class C:
    pass

class D:
    pass

class E:
    pass

class F:
    pass

class G:
    pass

# A collection of objects to create weak references to.
things = [C(), D(), E(), F(), G()]

# A collection of proxy objects.
proxies = []

# A collection of weak references.
refs = []

# A collection of objects to create weak references to that must be deleted
# first.
del_things = []

# Create a bunch of weak references to the objects in things, and append
# the weak references to refs.
for o in things:
    refs.append(weakref.ref(o))

# Create a bunch of weak references to random objects, and append the weak
# references to refs.
for i in range(len(things), len(things) + 10):
    o = C()
    refs.append(weakref.ref(
