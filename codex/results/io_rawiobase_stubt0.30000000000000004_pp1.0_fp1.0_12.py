import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self.file = file
        self.mode = mode
        self.closefd = closefd
        self.closed = False
        self.encoding = None
        self.errors = None
        self.newlines = None
        self.line_buffering = False
        self.softspace = False
        self.name = getattr(file, 'name', None)
        self.mode = getattr(file, 'mode', mode)
        self.closed = getattr(file, 'closed', False)
        self.encoding = getattr(file, 'encoding', None)
        self.errors = getattr(file, 'errors', None)
        self.newlines = getattr(file, 'newlines', None)
        self.line_buffering = getattr(file, 'line_buffering', False)
        self.softspace = getattr(file, 'softspace', False)
    def __repr__(self):
        return '<{}.{} {!r}, mode {
