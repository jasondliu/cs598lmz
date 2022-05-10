import io
class File(io.RawIOBase):
    def __init__(self, buff, header, offset=0):
        self.buff = buff
        self.header = header
        super(File, self).__init__()

    def __str__(self):
        return "File(%s) Header: %s" % (self.buff, self.header)

    def fileno(self):
        return None

    def seekable(self):
        return False

    def flush(self):
        return None

    def close(self):
        del self.buff[:]
        return None

    def readinto(self, b):
        ret = 0
        if len(self.buff) > 0:
            #print("B: %s, Type: %s, Size: %s, Req: %s, Offset: %s" % (b, type(b), b.nbytes, len(b), self.offset))

            if b.nbytes <= (len(self.buff) - offset):
                x = array.array("B",  self.buff[offset:b.nbytes])
            else:
               
