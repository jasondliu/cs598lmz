import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, object)
# Test io.RawIOBase.read()
assert isinstance(io.RawIOBase.read(), property)
# Test io.RawIOBase.readall()
assert isinstance(io.RawIOBase.readall(), property)
# Test io.RawIOBase.readinto()
assert isinstance(io.RawIOBase.readinto(), property)
# Test io.RawIOBase.readinto1()
assert isinstance(io.RawIOBase.readinto1(), property)
# Test io.RawIOBase.readline()
assert isinstance(io.RawIOBase.readline(), property)
# Test io.RawIOBase.readlines()
assert isinstance(io.RawIOBase.readlines(), property)
# Test io.RawIOBase.write()
assert isinstance(io.RawIOBase.write(), property)
# Test io.RawIOBase.writelines()
assert isinstance(io.RawIOBase.writelines(), property)
# Test io.RawIOBase.fileno()
assert isinstance(io.
