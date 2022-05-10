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

for attr in ('readline', 'readlines', '__iter__', 'close', 'flush', 'isatty',
             '__next__'):
    if hasattr(r, attr):
        raise TestFailed('%r has %r' % (r, attr))

if r.read(5) != b'abcde':

