import io
class File(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.cursor = 0
    def read(self, size):
        if self.cursor &gt;= len(self.data):
            return b''
        data = self.data[self.cursor:self.cursor+size]
        self.cursor += size
        return data
    def seek(self, offset, whence=0):
        if whence == 0:
            pass
        elif whence == 1:
            offset += self.cursor
        elif whence == 2:
            offset += len(self.data)
        else:
            raise ValueError
        if offset &gt; len(self.data) or offset &lt; 0:
            raise ValueError
        self.cursor = offset
        return self.cursor
    def tell(self):
        return self.cursor
    def close(self):
        pass    
</code>
This is not exactly a drop-in replacement, but should suffice.

