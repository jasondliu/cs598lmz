import io
class File(io.RawIOBase):
    def read(self, n=-1):
        # ...
        return super().read(n)

f = File()
f.read()

# io.RawIOBase.read()
# io.IOBase.read()
# object.__getattribute__(self, name)

# io.RawIOBase.read()
# io.IOBase.read()
# object.__getattribute__(self, name)

# io.RawIOBase.read()
# io.IOBase.read()
# object.__getattribute__(self, name)

# io.RawIOBase.read()
# io.IOBase.read()
# object.__getattribute__(self, name)

# io.RawIOBase.read()
# io.IOBase.read()
# object.__getattribute__(self, name)

# io.RawIOBase.read()
# io.IOBase.read()
# object.__getattribute__(self, name)

# io.RawIOBase.read()
# io.IOBase.read()
# object
