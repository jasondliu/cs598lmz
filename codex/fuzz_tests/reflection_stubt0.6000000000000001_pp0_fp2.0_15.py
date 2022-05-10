fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# these all fail with the same error
# fn.__code__ = 1
# fn.__code__ = (1, 1)
# fn.__code__ = (1, 1, 1)
# fn.__code__ = (1, 1, 1, 1)
# fn.__code__ = (1, 1, 1, 1, 1)
# fn.__code__ = (1, 1, 1, 1, 1, 1)
# fn.__code__ = (1, 1, 1, 1, 1, 1, 1)
# fn.__code__ = (1, 1, 1, 1, 1, 1, 1, 1)
# fn.__code__ = (1, 1, 1, 1, 1, 1, 1, 1, 1)
# fn.__code__ = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# fn.__code__ = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# fn.__code__ = (1,
