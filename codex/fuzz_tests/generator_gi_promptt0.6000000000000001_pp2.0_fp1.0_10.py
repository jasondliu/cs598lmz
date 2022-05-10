gi = (i for i in ())
# Test gi.gi_code.co_name is set correctly.
assert gi.gi_code.co_name == '<genexpr>'

# Test the new gi_frame attribute.
def f():
    return gi.gi_frame
assert f() is f.__globals__['gi'].gi_frame

# Test gi_frame is set correctly for coroutines.
async def f():
    pass
assert f.__code__.co_flags & 0x80
gi = f().gi_frame
assert gi.gi_code.co_name == 'f'
assert gi.f_code.co_name == 'f'
assert gi.f_code is f.__code__

# Test gi_frame is set correctly for asynchronous generators.
async def f():
    yield
gi = f().gi_frame
assert gi.gi_code.co_name == 'f'
assert gi.f_code.co_name == 'f'
assert gi.f_code is f.__code__

# Test gi_frame is set correctly for
