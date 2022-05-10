import weakref
# Test weakref.ref on user-defined objects.
# SF bug #306194
import gc


class C:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'C(%s)' % self.name
        return c

# Make sure we always have a cycle
def f():
    c = C('xyz')
    wr = weakref.ref(c)
    c.wr = wr
    return c


gc.enable()
for i in range(3):
    c = f()
    c = None
    gc.collect()
# Check that repr() still works on weak references.
# (SF bug #1185640)
import weakref


class C:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'C(%s)' % self.name
        return c


a = C('foo')
r = weakref.ref(a)
repr(r)
# Check that weakref() can be used on
