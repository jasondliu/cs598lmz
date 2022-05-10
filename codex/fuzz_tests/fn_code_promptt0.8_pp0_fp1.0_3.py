fn = lambda: None
# Test fn.__code__
s = fn.__code__

# Test fn.__code__.__dict__
class D:
    pass

d = D()
d.__dict__['__code__'] = None
