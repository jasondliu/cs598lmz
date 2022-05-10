fn = lambda: None
# Test fn.__code__, fn.__closure__, fn.__globals__,
# fn.__defaults__, fn.__dict__, etc. Raises AssertionError if any of
# the attributes is missing or has a wrong type.
def check(fn):
    if not hasattr(fn, "__code__"):
        raise AssertionError("{!r} has no code".format(fn))
    if not hasattr(fn, "__defaults__"):
        raise AssertionError("{!r} has no defaults".format(fn))
    assert isinstance(fn.__code__, types.CodeType)
    assert isinstance(fn.__defaults__, tuple)
    if not hasattr(fn.__code__, "co_filename"):
        raise AssertionError("{!r} has no filename".format(fn))
    if not hasattr(fn.__code__, "co_lineno"):
        raise AssertionError("{!r} has no lineno".format(fn))
    if not hasattr(fn.__code__,
