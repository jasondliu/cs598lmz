import io
# Test io.RawIOBase
f = open('/dev/null', 'r')
assert isinstance(f, io.RawIOBase)


# Test io.BufferedIOBase
f = open('/dev/null', 'rb')
assert isinstance(f, io.BufferedIOBase)


# Test io.TextIOBase
f = open('/dev/null', 'w')
assert isinstance(f, io.TextIOBase)


# Test io.FileIO
f = open('/dev/null', 'rb')
assert isinstance(f, io.FileIO)
