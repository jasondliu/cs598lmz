fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
try:
    fn()
except TypeError as e:
    pass

# Can't assign code to arbitrary objects - let's try a list:
list.__code__ = gi.gi_code
try:
    [][0]
except TypeError as e:
    pass

# No support for writing to the bytecode of a function
fn.__code__.co_code = b'1'
assert fn.__code__.co_code == b'|\x00d\x01\x17\x00\x00d\x02\x17\x01\x00'

# the repr should mention the class name
assert repr(gi).startswith(gi.__class__.__name__)

# Test generator-iterator equality
assert gi == gi
assert gi != (i for i in ())

# Test generator-iterator localization
gi1 = (i for i in ())
gi2 = (i for i in ())
gi_loc = locals()
gi_loc['gi1']
