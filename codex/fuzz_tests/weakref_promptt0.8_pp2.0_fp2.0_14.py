import weakref
# Test weakref.ref() and weakref.proxy()

# Create a couple of objects to be referenced.
class Foo(object):
    pass

a = Foo()
b = Foo()

# Create weak references to the objects.
aref = weakref.ref(a)
bref = weakref.ref(b)

# Create a weak reference to an object that does not exist
class C(object):
    pass

c = C()
cref = weakref.ref(c)
del c

# Create weak proxies to the objects.
aproxy = weakref.proxy(a)
bproxy = weakref.proxy(b)
assert aproxy == a
assert bproxy == b

# Create weak proxies to objects that do not exist
cproxy = weakref.proxy(cref)
assert cproxy is None
assert cproxy == cref()

# When called with a non-weakrefable argument, the functions return the
# argument
aproxy = weakref.proxy(3)
assert aproxy == 3

aproxy = weakref.proxy(None)
assert aproxy is None

ap
