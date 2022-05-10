fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
 
# An iterator cannot be a code object:
import dis

def fn():
    pass

it = (i for i in ())

try:
    fn.__code__ = it
except TypeError as e:
    assert str(e).startswith("iter() returned non-iterator")
else:
    assert False, "TypeError should have been raised"

# A code object cannot be a tuple:
fn = lambda: None

try:
    fn.__code__ = ()
except TypeError as e:
    assert str(e).startswith("code object is not iterable")
else:
    assert False, "TypeError should have been raised"

# An iterator cannot be a code object:
import dis

def fn():
    pass

it = (i for i in ())

try:
    fn.__code__ = it
except TypeError as e:
    assert str(e).startswith("iter() returned non-iterator")
else:
    assert False, "TypeError should have been raised"

# dir(code
