import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    pass

c = C()

# test weakref.ref()
r = weakref.ref(c)
assert r() is c
del c
assert r() is None

# test weakref.proxy()
p = weakref.proxy(c)
assert p is c
del c
try:
    p
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# test weakref.proxy() with callable
def f():
    pass

p = weakref.proxy(f)
assert p is f
del f
try:
    p
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# test weakref.proxy() with non-callable
class C:
    pass

c = C()
p = weakref.proxy(c)
assert p is c
del c
try:
    p
except ReferenceError:
    pass
else:
    raise Exception("expected ReferenceError")

# test weakref.proxy() with non-
