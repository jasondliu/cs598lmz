import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.f = open(name, mode)
        self.flock = threading.Lock()
        self.lock = threading.RLock()
        self.closed = False
    def __repr__(self):
        return '<File %s>' % self.name
    def __str__(self):
        return self.name
    def close(self):
        if not self.closed:
            self.closed = True
            self.f.close()
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        self.f.flush()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.mode in ('r', 'a+', 'r+')
    def read(self, n=-1):
        with self.lock:
            return self.f.read(n)
    def readinto(self
