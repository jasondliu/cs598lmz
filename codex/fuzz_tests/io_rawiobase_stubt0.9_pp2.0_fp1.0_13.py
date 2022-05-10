import io
class File(io.RawIOBase):
    def __init__(self,f):
        self.f=f
        self.name=f.name
        self.mode=f.mode
        self.fileno=f.fileno
        self.buffer=io.BufferedReader(f,io.DEFAULT_BUFFER_SIZE)
    def _close(self):
        self.buffer.close()
        self.buffer=None
        self.f=None
    def close(self):
        if self.buffer is not None:
            self._close()
    def flush(self):
        if self.f is not None:
            return self.f.flush()
    def fileno(self):
        if self.buffer is not None:
            return self.f.fileno()
        else:
            raise ValueError('stream is closed')
    def readable(self):return self.f.readable()
    def writable(self):return self.f.writable()
    def seekable(self):return self.f.seekable()
    def readline(self,limit=-1):
        read=self.
