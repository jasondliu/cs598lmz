import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._file = io.FileIO(path, "r")

    def readable(self):
        # We were opened for reading, so we know we're readable.
        return True

    def readinto(self, b):
        data = self._file.read(len(b))
        n = len(data)
        b[:n] = data
        return n
</code>
You can then do things like this:
<code>&gt;&gt;&gt; f = File('somefile.txt')
&gt;&gt;&gt; f.readable()
True
&gt;&gt;&gt; b = bytearray(100)
&gt;&gt;&gt; n = f.readinto(b)
&gt;&gt;&gt; b[:n]
b'This is some text'
</code>

