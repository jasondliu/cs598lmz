fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b"c", b"", b"", (), (), (), b"", b"", 0, b""
)
print(fn.__code__.co_varnames)

# Test fn.__code__.co_varnames with a tuple of bytes
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b"c", b"", b"", (), (), (), b"", b"", 0, (b"",)
)
print(fn.__code__.co_varnames)

# Test fn.__code__.co_varnames with a tuple of str
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b"c", b"", b"", (), (), (), b"", b"", 0, ("",)
)
print(fn.__code__.co_varnames)

# Test fn.__code__.co_varnames with a tuple of
