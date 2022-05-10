import io
# Test io.RawIOBase.readall()

class NewRawIOBase(io.RawIOBase):
    def readall(self):
        return b''

rawiobase = NewRawIOBase()
rawiobase.readall()
