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

# Test that the view is still usable after the file is closed.
view[0] = ord('a')

# Test that the file is still usable after the view is deleted.
print(f.read(1))

f.close()

# Issue #28063: test that RawIOBase.readinto() cannot be called
# with a wrong buffer type.
f = io.BufferedReader(File())
try:
    f.readinto('foobar')
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# Issue #30630: test that RawIOBase.readinto() can be called
# with a memoryview.
f.seek(0)
m = memoryview(bytearray(1))
f.readinto(m)

# Issue #30630: test that RawIOBase.readinto() cannot be called
# with an object that doesn't support the buffer protocol.
f.seek(0)
try:
    f.readinto(42)
except TypeError:
    pass
else:
    raise Exception("should
