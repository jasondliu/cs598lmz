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
</code>
Outputs:
<code>b'\xf1'
</code>

In Python3 io.RawIOBase.readinto is implemented as:
<code>def readinto(self, b):
    """Read up to len(b) bytes into b.

    Returns number of bytes read (0 for EOF).

    Raises BlockingIOError if the object is in non-blocking mode and has no data
        to read.
    """
    data = self.read(len(b))
    n = len(data)
    try:
        b[:n] = data
    except TypeError as err:
        import array
        if not isinstance(b, array.array):
            raise err
        b[:n] = array.array(b'b', data)
    return n
</code>

