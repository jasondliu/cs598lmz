import weakref
# Test weakref.ref()
class foo(object):
    pass
f = foo()
f.bar = 1
wr = weakref.ref(f)
