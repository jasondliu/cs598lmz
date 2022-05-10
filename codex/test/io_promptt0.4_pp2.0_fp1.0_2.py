import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        return b'abcdefghijklmnop'[:size]
    def write(self, b):
        return len(b)

try:
    io.RawIOBase.name
except AttributeError:
    pass
else:
    raise TestFailed('io.RawIOBase.name should not exist')

r = MyRawIO()
for attr in ('read', 'readinto', 'write', 'fileno', 'seek', 'tell', 'truncate'):
    if not hasattr(r, attr):
        raise TestFailed('%r lacks %r' % (r, attr))

