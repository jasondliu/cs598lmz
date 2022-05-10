fn = lambda: None
# Test fn.__code__ gets set on assignment.
fn.__code__ = compile("x = 42", "<string>", "exec")
assert fn.__code__.co_filename == "<string>"

# Test fn.__code__ is writeable.
del fn.__code__
fn.__code__ = compile("x = 42", "<string>", "exec")
assert fn.__code__.co_filename == "<string>"

# Test fn.__code__ can be None
fn = lambda: None
del fn.__code__
assert fn.__code__ is None


def func_with_kwlist(a, b=5, *args, c, d=6, **kwargs):
    return a + b + c + d + len(args) + len(kwargs)


assert func_with_kwlist._anonymous.__kwdefaults__ == dict(b=5, d=6)
assert func_with_kwlist.__kwdefaults__ == dict(b=5, d=6)

# Test that closures containing builtins linked to old versions of the
# __builtins__ module
