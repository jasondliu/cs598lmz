import io
class File(io.RawIOBase):
    def read(self, n=-1): return ''
    def write(self, b): return len(b)

open = File
