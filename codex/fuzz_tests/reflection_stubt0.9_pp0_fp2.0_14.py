fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.gi.gi_code
assert fn.__code__ is fn.gi.gi_code


# attributes of code objects
assert fn.__code__.co_argcount == 0
try:
    fn.__code__.co_argcount = 42
except TypeError:
    pass
else:
    raise Exception("assigning to co_argcount should have failed")
assert fn.__code__.co_kwonlyargcount == 0
try:
    fn.__code__.co_kwonlyargcount = 42
except TypeError:
    pass
else:
    raise Exception("assigning to co_kwonlyargcount should have failed")

assert fn.__code__.co_nlocals == 0
try:
    fn.__code__.co_nlocals = 42
except TypeError:
    pass
else:
    raise Exception("assigning to co_nlocals should have failed")
assert fn.__code__.co_stacksize == 1
try:
    fn.__code__.co_stacksize = 42
except TypeError:
    pass

