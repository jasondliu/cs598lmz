import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.name = f.name
        self.mode = f.mode
        self.closed = f.closed
        self.encoding = f.encoding
        self.errors = f.errors
        self.newlines = f.newlines
        self.line_buffering = f.line_buffering
        self.seekable = f.seekable
        self.readable = f.readable
        self.writable = f.writable
    def __repr__(self):
        return '<File %r>' % self.f
    def __str__(self):
        return str(self.f)
    def __getattr__(self, name):
        return getattr(self.f, name)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
    def __del__(self):
        self.close()
    def close(self):
        self.f.close()
    def fileno(self
