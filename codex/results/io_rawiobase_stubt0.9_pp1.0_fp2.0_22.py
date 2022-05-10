import io
class File(io.RawIOBase):
    def __init__(self, deflateFrames_obj, delimiter='\n'):
        self.delimiter = delimiter
        self.dfl = deflateFrames_obj
        self.buffer = []

    def read(self, count=-1):
        if count < 0:
            delim_len = len(self.delimiter)
            while self.dfl.next(1):
                bytes = self.next_bytes(delim_len)
                self.buffer.append(bytes)
                if bytes == self.delimiter:
                    break
            buf = b''.join(self.buffer)
            self.buffer = []
            return buf

        buf = bytes()
        while buf < count and self.dfl.next(1):
            bytes = self.next_bytes(min(count-len(buf),1024), 1)
            self.buffer.append(bytes)
            buf += bytes
        if buf == count:
            buf2 = b''.join(self.buffer)
            self.buffer = []
        else:
            buf2 = b''.join(
