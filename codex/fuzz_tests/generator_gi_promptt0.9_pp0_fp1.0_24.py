gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom

class OldStyle:
    pass

class NewStyle(object):
    pass

# First test that new-style instances don't have any '__dict__'
# attributes.
obj = OldStyle()
# Test type(obj).__dict__.
# Test vars(obj).
# Test obj.__dict__.
# Test type(obj).__dict__ is obj.__dict__
# Test obj.__class__.__dict__.

obj = NewStyle()
# Test type(obj).__dict__.
# Test vars(obj).
# Test obj.__dict__.
# Test type(obj).__dict__ is obj.__dict__
# Test obj.__class__.__dict__.


# Now test with new-style instances with a __dict__ attribute.
class NewStyle2(object):
    def __init__(self):
        self.__dict__ = {1: 2}

def f():
    x =
