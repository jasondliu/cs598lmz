import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size=-1):
        return open(self.name, 'rb').read()
    def readable(self):
        return True
# Now let's suppose that you want to construct a file-like object that wraps a file
# and adds logging. Here's an implementation:

class LoggingFile(io.RawIOBase):
    def __init__(self, name):
        self.f = open(name, 'rb')

    def read(self, size=-1):
        data = self.f.read(size)
        print('read({!r}) -> {!r}'.format(size, data))
        return data

    def readable(self):
        return True
# This implementation is pretty simple, but it works.

# Now suppose you want to write a file-like object that wraps another file, but encrypts all
# content before it is written. Here's what that would look like:

class EncryptingFile(io.RawIOBase):
    def __init__(self, name
