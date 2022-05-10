import io
# Test io.RawIOBase
#
# Issue #7155
import io, threading

data = 'hello world\n'

class TestRawIO(io.RawIOBase):
    def __init__(self):
        self.read_buf = threading.local()
    def readinto(self, b):
        if not hasattr(self.read_buf, 'data'):
            try:
                self.read_buf.data = data[self.tell():]
            except ValueError:
                raise EOFError()
        count = len(b)
        if count > len(self.read_buf.data):
            count = len(self.read_buf.data)
        b[:count] = self.read_buf.data[:count]
        self.read_buf.data = self.read_buf.data[count:]
        return count

def run_threads(func):
    def worker(t, s):
        with s:
            func()
    threads = [
        threading.Thread(target=worker, args=(i, t_stream))
        for
