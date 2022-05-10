import io
class File(io.RawIOBase):
    def __init__(self, file, block_size=io.DEFAULT_BUFFER_SIZE):
        self.file = file
        self.block_size = block_size
        self.buffer = b''

    def readable(self):
        return True

    def _read1(self, n=-1):
        while not self.closed:
            try:
                b = self.file.read(n)
            except (BlockingIOError, InterruptedError):
                continue
            else:
                if b:
                    return b
                else:
                    raise EOFError
            break
        return b''

    def read(self, n=-1):
        # code from io.FileIO.read()
        if n is None:
            n = -1
        if not self.readable():
            raise OSError("File not open for reading")
        if n < 0:
            # Read until EOF
            n = 999999999999999999
            result = self.buffer
            self.buffer = b''
            while True:
                b = self._read1
