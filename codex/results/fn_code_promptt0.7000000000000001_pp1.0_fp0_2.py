fn = lambda: None
# Test fn.__code__.co_flags & 0x28 != 0
fn.__code__ = type(fn.__code__)()
fn.__code__.co_flags = 0x28
try:
    fn()
except TypeError:
    pass
else:
    assert False

# Test fn.__code__.co_code
fn = lambda: None
# Test fn.__code__.co_code is not None
fn.__code__ = type(fn.__code__)()
fn.__code__.co_code = b"\x00\x01\x02"
fn.__code__.co_flags = 0
try:
    fn()
except TypeError:
    pass
else:
    assert False

# Test fn.__code__.co_code is not a string
fn.__code__.co_code = 0xdeadbeef
try:
    fn()
except TypeError:
    pass
else:
    assert False

# Test fn.__code__.co_code is not a bytes
fn.__code__.co_code = "deadbe
