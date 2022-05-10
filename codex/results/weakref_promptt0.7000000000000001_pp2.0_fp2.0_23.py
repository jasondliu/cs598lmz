import weakref
# Test weakref.ref()
class foo(object):
    pass
f = foo()
f.bar = 1
wr = weakref.ref(f)
print wr.__module__
print wr.__class__
print wr.__call__
print wr.__str__
print wr.__repr__
wr.__call__
wr.__str__
wr.__repr__
