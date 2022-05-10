import io
class File(io.RawIOBase):
    def writable(self):
        return True
    def write(self, data):
        print('Writing data: {!r}'.format(data))
        return len(data)

f = File()
f.writable()

f.write(b'Hello, Python!')

class File2(io.RawIOBase):
    def writable(self):
        return True
    def write(self, data):
        print('Writing data: {!r}'.format(data))
        return len(data)

f = File2()

f.write(b'Hello, Python!')

f.isatty()
f.readable()

f.fileno()
f.flush()
f.readinto(b'123')


f.seek(10)
f.tell()

f.truncate()

# def __init__(self, file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
#    super().__init__(file, mode, buffering,
