import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, object)
# Test io.RawIOBase.read()
assert isinstance(io.RawIOBase.read, collections.abc.Callable)
try:
    io.RawIOBase.read()
except TypeError:
    pass
else:
    raise RuntimeError
# Test io.RawIOBase.readall()
assert isinstance(io.RawIOBase.readall, collections.abc.Callable)
try:
    io.RawIOBase.readall()
except TypeError:
    pass
else:
    raise RuntimeError
# Test io.RawIOBase.readinto()
assert isinstance(io.RawIOBase.readinto, collections.abc.Callable)
try:
    io.RawIOBase.readinto()
except TypeError:
    pass
else:
    raise RuntimeError
# Test io.RawIOBase.readinto1()
assert isinstance(io.RawIOBase.readinto1, collections.abc.Callable)
try:
    io.RawIOBase.readinto1()
except TypeError:
