fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #7391: do not crash if __code__ is set to a non-code object.
def f():
    pass
try:
    f.__code__ = 42
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue #7391: do not crash if __code__ is set to a non-code object.
try:
    f.__code__ = "hello"
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue #7391: do not crash if __code__ is set to a non-code object.
try:
    f.__code__ = object()
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue #7391: do not crash if __code__ is set to a non-code object.
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue #7391: do not crash if
