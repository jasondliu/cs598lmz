import io
class File(io.RawIOBase):
    def __init__(self):
        pass

f = File()
f

class Socket(io.RawIOBase):
    def __init__(self):
        self.connected = False

    #def close(self):
    #    self.connected = False

    def readable(self):
        return True

    def writable(self):
        return True

    def getvalue(self):
        return ''

s = Socket()
s.connected = True
s
assert not s.closed
assert not s.isatty()
assert not s.seekable()

bytes = s.read(10)
assert len(bytes) == 10
bytes = s.read(10)
assert len(bytes) == 0
assert s.getvalue() == ''
assert s.writable()
print('OK')
