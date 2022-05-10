import weakref
# Test weakref.ref()
class A:
    pass
a = A()
wr = weakref.ref(a)
assert wr() is a
a = None
assert wr() is None
# Test weakref.proxy()
class A:
    pass
a = A()
wp = weakref.proxy(a)
assert wp is a
a = None
try:
    wp
except ReferenceError:
    pass
