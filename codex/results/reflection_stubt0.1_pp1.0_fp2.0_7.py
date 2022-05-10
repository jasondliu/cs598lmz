fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22897: Check that the __code__ attribute of a built-in function
# is not writable.
def f():
    pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ = None should have raised TypeError")

# Issue #22897: Check that the __code__ attribute of a built-in method
# is not writable.
try:
    [].append.__code__ = None
except TypeError:
    pass
else:
    print("[].append.__code__ = None should have raised TypeError")

# Issue #22897: Check that the __code__ attribute of a built-in method
# is not writable.
try:
    {}.get.__code__ = None
except TypeError:
    pass
else:
    print("{}.get.__code__ = None should have raised TypeError")

# Issue #22897: Check that the __code__ attribute of a built-in method
# is not writable
