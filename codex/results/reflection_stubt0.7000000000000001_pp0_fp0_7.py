fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Make the "co_name" of fn.__code__ be a new-style string, and
# check that the repr() of fn.__code__ doesn't crash.
fn.__code__.co_name = 'name'
repr(fn.__code__)

# Check that the repr() of a code object doesn't crash.
def f(): pass
repr(f.__code__)

# Check that the repr() of a module doesn't crash.
import sys
repr(sys)

# Check that the repr() of a method doesn't crash.
repr(repr)


# Check that the repr() of a class doesn't crash.
class C: pass
repr(C)


# Check that the repr() of a method-wrapper object doesn't crash.
getattr(C, '__repr__')

# Check that the repr() of a traceback object doesn't crash.
def g():
    raise Exception
try:
    g()
except:
    import sys
    tb = sys.exc_info()[
