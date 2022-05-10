fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Issue #23692: make sure we don't crash on a read-only object
# when a custom metaclass is used
class ReadOnlyMeta(type):
    def __delattr__(self, attr):
        raise AttributeError("you cannot delete this attribute")

class ReadOnly(metaclass=ReadOnlyMeta):
    pass

try:
    del ReadOnly.__dict__
except AttributeError:
    pass
else:
    print("del ReadOnly.__dict__ should have raised AttributeError")

