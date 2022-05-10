import io
class File(io.RawIOBase):
    def __init__(self, path, byteorder='<'):
        if byteorder not in ['<', '>', '@']:
            raise ValueError('invalid byteorder')
        self.byteorder = byteorder
        self.path = path
        self.file = open(path, 'wb')

    # Read a number of bytes.
    def read(self, n):
        return self.file.read(n)

    # Read one byte.
    def read1(self, n):
        return self.file.read(n)

    # Read a byte instant.
    def read_u8(self):
        return self.file.read(1)[0]

    # Read a short.
    def read_u16(self):
        return self.unpack_from('<H', 2)[0]

    # Read a long.
    def read_u32(self):
        return self.unpack_from('<I', 4)[0]

    # Read a double.
    def read_double(self):
        return self.unpack_from('
