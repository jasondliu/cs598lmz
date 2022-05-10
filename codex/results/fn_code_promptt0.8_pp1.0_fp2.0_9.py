fn = lambda: None
# Test fn.__code__.co_argcount on a built-in callable
try:
    set.__code__.co_argcount
except AttributeError:
    pass
else:
    raise TestFailed("built-in callable has __code__.co_argcount attribute")

# Test fn.__name__ on a built-in callable
try:
    set.__name__
except AttributeError:
    pass
else:
    raise TestFailed("built-in callable has __name__ attribute")

# We'll call this on non-callables, including classes and instances, to
# make sure it doesn't find a __code__ attribute where it shouldn't.
def test_no_code(obj):
    try:
        obj.__code__
    except AttributeError:
        pass
    else:
        raise TestFailed(
            "{obj!r} instance unexpectedly has __code__ attribute".format(
                obj=obj
            )
        )

test_no_code(None)
test_no_code(1)
test_no_code(1.0)
