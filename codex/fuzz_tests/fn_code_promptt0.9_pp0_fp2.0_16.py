fn = lambda: None
# Test fn.__code__
fn.__code__

with pytest.raises(TypeError):
    fn.__code__.co_argcount

with pytest.raises(TypeError):
    getcallargs(fn)

# Test fn.__code__.co_code
with pytest.raises(ValueError):
    fn.__code__.co_code = b"hello"

with pytest.raises(ValueError):
    fn.__code__.co_code = b"\x01"

assert fn.__code__.co_code == b""

with pytest.raises(NotImplementedError):
    fn.__code__.co_flags

with pytest.raises(TypeError):
    getattr(fn.__code__, "co_stacksize")
with pytest.raises(TypeError):
    getattr(fn.__code__, "co_name")
with pytest.raises(TypeError):
    getattr(fn.__code__, "co_lnotab")
with pytest.raises(
