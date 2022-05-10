import weakref
# Test weakref.ref
class C(object):
    pass

c = C()
wr = weakref.ref(c)
assert wr() is c
del c
assert wr() is None
# Test weakref.proxy
class C(object):
    pass

c = C()
wr = weakref.proxy(c)
assert wr is c
del c
try:
    wr
except ReferenceError:
    pass
