import io
class File(io.RawIOBase):
    name = None
    mode = None
    closed = None
    newlines = None
    softspace = None
    class _io:
        BlockingIOError = None
        UnsupportedOperation = None
        __init__ = None
        __enter__ = None
        __exit__ = None
        close = None
        fileno = None
        flush = None
        isatty = None
        read = None
        readable = None
        readline = None
        readlines = None
        seek = None
        seekable = None
        tell = None
        truncate = None
        writable = None
        write = None
        writelines = None
        __init__ = None
    def __init__(self, *args, **kwargs): pass
    def __enter__(self, *args, **kwargs): pass
    def __exit__(self, *args, **kwargs): pass
    def __iter__(self, *args, **kwargs): pass
    def close(self, *args, **kwargs): pass
    def closed(self, *args, **kwargs
