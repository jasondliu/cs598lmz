import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name

    def close(self):
        print(f'closing {self.name}')

    def read(self, size=-1):
        return b'a' * size


f = File('foo')
print(f.read(5))
f.close()

# file-like objects can be used with the with statement

from contextlib import contextmanager

@contextmanager
def file(name):
    try:
        f = File(name)
        yield f
    finally:
        f.close()
    
with file('foo') as f:
    print(f.read(5))

# you can also use the contextlib module's closing function to avoid writing
# the finally clause

from contextlib import closing

with closing(File('foo')) as f:
    print(f.read(5))

# the contextlib module has a few other useful functions, such as suppress,
# which suppresses specified exceptions

from contextlib import suppress

with suppress(ValueError):
    print
