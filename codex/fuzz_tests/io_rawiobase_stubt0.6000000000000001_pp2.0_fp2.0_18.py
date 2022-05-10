import io
class File(io.RawIOBase):
    def __init__(self, fp):
        self.fp = fp
        self.read = fp.read
        self.write = fp.write
        self.fileno = fp.fileno
        self.seek = fp.seek
        self.tell = fp.tell
        self.truncate = fp.truncate
        self.flush = fp.flush
        self.isatty = fp.isatty

import functools

def fileno(f):
    try:
        return f.fileno()
    except AttributeError:
        return f.fp.fileno()

def _wrap_close(f, close):
    @functools.wraps(f)
    def _close(*args, **kwargs):
        res = f(*args, **kwargs)
        close()
        return res
    return _close

def _wrap_close_fd(f, fd):
    @functools.wraps(f)
    def _close(*args, **kwargs):
        res
