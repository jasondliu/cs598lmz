fn = lambda: None
# Test fn.__code__ to make sure it's consistent:
code_fn.__code__ is code(fn)

globals().update(locals())
