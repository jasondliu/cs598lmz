import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def read(self, n=-1):
        with open(self.filename, 'rb') as fd:
            return fd.read(n)

    def readable(self):
        return True

    def writable(self):
        return False

f = File("file.txt")
print(f.read())

print(f.readable())
print(f.writable())

# For ABC, I implemented Callable class for the first time.
# It checks if an object is callable.

from collections.abc import Callable
def callable_obj():
    pass

print(callable(callable_obj))
print(callable(f))
print(isinstance(callable_obj, Callable))

# The final ABC I have implemented is Iterable.
# It checks if an object is iterable.

from collections.abc import Iterable

def iterable_obj():
    yield 1
    yield 2

print(
