import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f


assert view == memoryview(b"x")
assert buffer(view) is view

# Get a writable non-resizable view.
view = memoryview(b"x" * 100)
promote_type = type(view)

v = buffer(view)
assert v is not view
assert v is not buffer(view)
assert v is not buffer(v)
assert type(v) is type(buffer(v)) is promote_type

assert v.obj is view.obj
assert v.itemsize == view.itemsize
assert v.nbytes == view.nbytes
assert len(v) == len(view)
assert v.ndim == view.ndim


# Get a writable resizable view.
view = memoryview(bytearray(b"x" * 100))
promote_type = type(view)

v = buffer(view)
assert v is not view
assert v is not buffer(view)
assert v is not buffer(v)
assert type(v) is type(buffer(v)) is promote_type

assert v.obj is view
