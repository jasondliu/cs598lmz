import weakref
# Test weakref.ref(1, 1) for failure mode before we set __doc__ and __name__
W = weakref.ref(1, 1)
assert W.__doc__ == None
assert W.__name__ == None

# Make sure the length of __doc__ is 10+ the length of __name__
def add_prefix(prefix):
    def hook(fn, name, doc=None):
        if doc:
            f = lambda r, fn=fn, doc=prefix+doc: fn(r, doc)
        else:
            f = lambda r, fn=fn: fn(r)
        r = weakref.ref(1, f)
        r.__name__ = 'r'
        r.__doc__ = prefix+name
        assert len(r.__name__) + 10 == len(r.__doc__)
        return r
    return hook

# Check weakref.ref and weakref.proxy

# weakref.ref:
if hasattr(weakref, 'ReferenceType'):
    assert weakref.ReferenceType == weakref.ref
r = weakref.ref
