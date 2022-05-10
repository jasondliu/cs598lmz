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
print(view)

f = io.BufferedReader(File())
del f
try:
    f.read(1)
except ValueError:
    print("ValueError")
f = io.BufferedReader(File())
print(f.readable())
del f
try:
    f.readable()
except ValueError:
    print("ValueError")

# A simple finalization test.
class C:
    def __del__(self):
        print("del")

f = io.BufferedReader(C())
del f

# A test for readinto() with a negative argument
f = io.BufferedReader(io.BytesIO(b"hello"))
try:
    f.readinto(-1)
except ValueError:
    print("ValueError")

# Test for passing None as the underlying object.
try:
    f = io.BufferedReader(None)
except TypeError:
    print("TypeError")

# A test for passing a number as the underlying object.
try:
    f = io.BufferedReader(1)
except TypeError
