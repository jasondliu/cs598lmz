import lzma
lzma.LZMAFile(open("dataguide.lzma", "w")).close()
os.remove("dataguide.lzma")


class StreamConsolidator(object):

    __slots__ = ('f', 'closed', '_file_pos')

    def __init__(self, file):
        self.f = file
        self.closed = False
        self._file_pos = 0

    def write(self, chunk):
        if self.closed:
            raise ValueError("file already closed for writing")
        if self.f is None:
            return
        self.f.write(chunk)
        self._file_pos += len(chunk)

    def read(self, amount):
        if self.closed:
            raise ValueError("file already closed for reading")
        if self.f is None:
            return b'\x00' * amount
        buf = self.f.read(amount)
        if len(buf) < amount:
            raise EOFError()
        self._file_pos += len(buf)
        return
