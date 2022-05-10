from bz2 import BZ2Decompressor
BZ2Decompressor

def _dbg(a):
    print(a)

class _Header:
    def __init__(self, fileobj, offset, parent):
        self.fileobj = fileobj
        self.offset = offset
        self.parent = parent

    def __str__(self):
        return "<pvm header at %d>" % self.offset

    def __repr__(self):
        return str(self)

    def __getitem__(self, name):
        return self.__dict__[name]

    def _read(self, offset, size):
        self.fileobj.seek(offset)
        s = self.fileobj.read(size)
        if len(s) != size:
            raise ValueError("Unable to read %d bytes at %d" % (size, offset))
        return s

    def _read_int(self, offset, size):
        return int.from_bytes(self._read(offset, size), byteorder='little')

    def _read_str(self, offset, size):
        return str(self._read(
