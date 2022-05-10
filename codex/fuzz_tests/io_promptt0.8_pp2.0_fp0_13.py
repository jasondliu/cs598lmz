import io
# Test io.RawIOBase interface

class T(io.RawIOBase):
    def __init__(self):
        self.closed = 0
    def read(self,n):
        return 'x' * n
    def write(self,s):
        pass
    def close(self):
        self.closed = 1

t = T()

print t.closed
t.close()
print t.closed

print t.read(2)
print t.read(1000)
print t.readline(10)
print t.readline()

print repr(t.readlines())
t.writelines(['foo','bar','baz'])

t.seek(0)

t.tell()

t.seekable()
t.readable()
t.writable()

t.isatty()

t.flush()
