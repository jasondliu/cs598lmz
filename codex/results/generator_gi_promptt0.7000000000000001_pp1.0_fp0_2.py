gi = (i for i in ())
# Test gi.gi_code not being int, even though that's the type of
# the attribute on CPython.
gi.gi_code = object()

class cls(object):
    def __init__(self):
        self.attr = None

cls_inst = cls()

def f():
    pass

# Test f.__globals__ not being dict.
f.__globals__ = object()

# Test f.__defaults__ not being tuple, even though that's the type of
# the attribute on CPython.
f.__defaults__ = object()

# Test f.__code__ not being types.CodeType.
f.__code__ = object()

# Test f.__closure__ not being tuple, even though that's the type of
# the attribute on CPython.
f.__closure__ = object()

# Test f.__annotations__ not being dict, even though that's the type of
# the attribute on CPython.
f.__annotations__ = object()

f.attr = object()

def get_attr(obj, attr
