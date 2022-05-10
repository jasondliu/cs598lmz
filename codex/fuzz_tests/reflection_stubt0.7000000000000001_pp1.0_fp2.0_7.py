fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Code objects are supposed to be immutable
code = fn.__code__
code.co_filename = 'xxx'

# Generators should raise an error if their frames are accessed
# (such as by calling co_filename on them)
def f():
    def g():
        yield
    try:
        g().send(None)
    except StopIteration:
        pass
    else:
        raise AssertionError

# Generators should raise an error if their frames are modified
def f():
    def g():
        yield
    try:
        g().gi_frame.f_code = None
    except AttributeError:
        pass
    else:
        raise AssertionError

# Generators should raise an error if their frames are accessed
# (such as by calling gi_frame on them)
def f():
    def g():
        yield
    try:
        g().gi_frame
    except AttributeError:
        pass
    else:
        raise AssertionError

# Generators should be allowed to delete their frames
def f():

