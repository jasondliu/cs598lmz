fn = lambda: None
# Test fn.__code__ code object is not writable
# (which used to be a bug in Python 2)
test_fn.__code__ = type(test_fn.__code__)(
    0, 15, 1, 0, b'<string>', b'<module>',
    b"# test", (None,), (),
    b"", b"", 0, b""
)
assert test_fn.__code__.co_filename == '<string>'
assert test_fn.__code__.co_argcount == 0
# co_name should be set to "<module>" for functions defined at module scope
assert test_fn.__code__.co_name == '<module>'

# Bytes literals in exec
exec(b"a = b'123'")
assert a == b'123'

# Function annotations
def fn(a: 'foo') -> 'bar':
    return a
assert fn.__annotations__ == {'a': 'foo', 'return': 'bar'}

# Exec
exec("a = 1")
assert a == 1

exec("a = 1
