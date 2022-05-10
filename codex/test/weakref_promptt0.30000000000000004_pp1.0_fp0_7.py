import weakref
# Test weakref.ref(x) == weakref.ref(x)

import weakref

class Foo(object):
    pass

f = Foo()

assert weakref.ref(f) == weakref.ref(f)
assert weakref.ref(f) is not weakref.ref(f)

# Test weakref.ref(x) != weakref.ref(y)

import weakref

class Foo(object):
    pass

f = Foo()
g = Foo()

assert weakref.ref(f) != weakref.ref(g)
assert weakref.ref(f) is not weakref.ref(g)

# Test weakref.ref(x) == x

import weakref

class Foo(object):
    pass

f = Foo()

assert weakref.ref(f) == f
assert weakref.ref(f) is not f

# Test weakref.ref(x) != y

import weakref

class Foo(object):
    pass

f = Foo()
