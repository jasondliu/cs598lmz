fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(lambda: 0).__code__
print(fn.__code__)
gi.__code__ = fn.__code__

class Foo(metaclass=type): pass
Foo.__weakrefoffset__ = None
del Foo

try:
    import _ssl
except ImportError:
    pass
else:
    _ssl.SSLContext.__weakrefoffset__ = None
    del _ssl
