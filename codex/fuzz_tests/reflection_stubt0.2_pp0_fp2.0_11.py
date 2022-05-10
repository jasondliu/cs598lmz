fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not copied when the function is called
# (see issue #17073).
import copy
def f():
    pass
f.__code__ = copy.copy(f.__code__)
f()

# Test that the code object is not copied when the function is called
# (see issue #17073).
import copy
def f():
    pass
f.__code__ = copy.deepcopy(f.__code__)
f()

# Test that the code object is not copied when the function is called
# (see issue #17073).
import copy
def f():
    pass
f.__code__ = copy.copy(f.__code__)
f()

# Test that the code object is not copied when the function is called
# (see issue #17073).
import copy
def f():
    pass
f.__code__ = copy.deepcopy(f.__code__)
f()

# Test that the code object is not copied when the function is called
# (see issue #1707
