import io
class File(io.RawIOBase):
    #at some point have this work over Network
    def __init__(self, filepath):
        self.filepath = filepath
        #support reading non bin file?
        

class BitInput(io.RawIOBase):
    def __init__(self, file, bits=16):
        self.bits = bits
        self.buffer = []
        self.file = input
    
    def close(self):
        pass
    
    def readable(self):
        return True
    
    def seekable(self):
        return True
    
    def tell(self):
        return self.file.tell() * 8 + len(self.buffer)
    
    def seek(self, offset, whence=0):
        if whence == 0:
            self.file.seek(offset // 8)
            self.buffer = []
        else:
            raise ValueError("Argument 2 to seek has to be 0 since seeking relative to current")

    def readinto(self, b):
        raise NotImplementedError

    def _read_bit(self):
        if self.
