fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")


# type safety of __code__
try:
    fn.__code__ = "string"
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")
