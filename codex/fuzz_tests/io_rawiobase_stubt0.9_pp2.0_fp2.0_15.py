import io
class File(io.RawIOBase):
    '''
    DelayedFile implements a file like interface for the
    Buffer class. This can be useful when the Buffer instance is
    an actual file on a remote host and the consumer for the
    file requires a file like object to interface with.
    '''
    def __init__(self,buffer):
        io.RawIOBase.__init__(self)
        self.buffer = buffer
        self.position = 0

    def read(self,length=0):
        buffer=self.buffer.rread(self.position,length)
        self.position+=len(buffer)
        return buffer
