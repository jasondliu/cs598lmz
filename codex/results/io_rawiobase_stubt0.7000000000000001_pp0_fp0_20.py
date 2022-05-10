import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self.file = file
        self.mode = mode
    def readinto(self, b):
        n = len(b) # aiming to read n bytes
        chunk = self.file.read(n)
        m = len(chunk) # number of bytes effectively read
        try:
            b[:m] = chunk
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:m] = array.array(b'b', chunk)
        return m

f = open('/dev/urandom', 'rb')
# Create an io.BytesIO object from the file handle
b = io.BytesIO(f)

# Create a new file object from the io.BytesIO object
g = File(b)
print(g.read(10))

# After reading from g, the position of b is updated
print(b.tell())

g.seek(0)
print(b.tell())

g.seek(
