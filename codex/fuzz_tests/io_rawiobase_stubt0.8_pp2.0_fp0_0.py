import io
class File(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        v = self.read()
        n = len(v)
        b[:n] = v
        return n
    def writeable(self):
        return False
    def writelines(self, lines):
        for line in lines:
            self.write(line)
    def __exit__(self, *args):
        self.close()
class BufferedReader(File): # abstract
    def __init__(self, raw, buffer_size=io.DEFAULT_BUFFER_SIZE):
        self.buffer_size = buffer_size
        self._read_lock = _thread.allocate_lock()
        self._write_lock = _thread.allocate_lock()
    def read(self, n=-1):
        if n < 0:
            return self.readall()
        with self._read_lock:
            if n >= len(self._read_buf):
                return self._read_buf + self._read1(n - len(self._read_buf))

