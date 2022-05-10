fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# bpo-33505: The test failed with the following error message:
# "TypeError: a generator cannot have a code object"
try:
    fn()
except TypeError:
    pass
else:
    raise AssertionError("TypeError not raised")

# bpo-33505: The test failed with the following error message:
# "RuntimeError: generator ignored GeneratorExit"
try:
    gi.close()
except RuntimeError:
    pass
else:
    raise AssertionError("RuntimeError not raised")

# bpo-33505: The test failed with the following error message:
# "RuntimeError: generator ignored GeneratorExit"
try:
    gi.__del__()
except RuntimeError:
    pass
else:
    raise AssertionError("RuntimeError not raised")

# bpo-33505: The test failed with the following error message:
# "RuntimeError: generator ignored GeneratorExit"
try:
    gi.throw(StopIteration)
except RuntimeError:
    pass
else:
    raise AssertionError("
