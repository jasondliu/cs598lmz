import weakref
# Test weakref.ref()
def f():
    return 42

x = f()
assert x == 42
r = weakref.ref(x)
assert r() == 42
del x
assert r() == 42

def g():
    return [1, 2, 3]

x = g()
assert x == [1, 2, 3]
r = weakref.ref(x)
assert r() == [1, 2, 3]
del x
assert r() == [1, 2, 3]

def h():
    return (1, 2, 3)

x = h()
assert x == (1, 2, 3)
r = weakref.ref(x)
assert r() == (1, 2, 3)
del x
assert r() == (1, 2, 3)

def i():
    return {'a': 1, 'b': 2}

x = i()
assert x == {'a': 1, 'b': 2}
r = weakref.ref(x)
assert r() == {'a': 1, 'b': 2}
del x
assert r
