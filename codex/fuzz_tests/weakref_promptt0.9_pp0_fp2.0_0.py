import weakref
# Test weakref.ref(cmp) keyed-on dicts
# from cStringIO import StringIO

class C(object):
    def fin(self, ref=None):
        global broken
        broken.append(ref)


def dummy(x=None):
    return x

# Check expected behaviour...
for base in [int, C]:
    # Normal use of weakref
    x = base(42)
    global broken
    broken = []
    r = weakref.ref(x, dummy)
    assert r() is x
    x = None
    gc.collect(); gc.collect(); gc.collect();
    assert len(broken) == 1
    assert r() is x
    r = None
    gc.collect(); gc.collect(); gc.collect();
    # Check that the callback works when a weakref falls out of scope
    x = base(42)
    broken = []
    weakref.ref(x, broken.append)
    x = None
    gc.collect(); gc.collect(); gc.collect();
    assert len(broken) == 1
