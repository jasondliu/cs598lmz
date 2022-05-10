import io
class File(io.RawIOBase):
    '''
    A file-like object that allows to read from a file
    and write to a file in a different thread.
    '''
    def __init__(self, file):
        self.file = file
        self.buffer = None
        self.read_eof = False
        self.write_eof = False
        self.reader_lock = Lock()
        self.writer_lock = Lock()

    def readable(self):
        return True

    def writable(self):
        return True

    def read(self, size=-1):
        if size == 0:
            return b''
        if self.read_eof:
            return None
        while True:
            with self.reader_lock:
                if self.buffer is not None:
                    if size < 0 or size > len(self.buffer):
                        data = self.buffer
                        self.buffer = None
                    else:
                        data = self.buffer[:size]
                        self.buffer = self.buffer[size:]
                    return data
                if self.write_eof:
                    self
