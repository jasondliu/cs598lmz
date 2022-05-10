import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb', closefd=True):
        self.mode = mode
        self.name = filename
        self.closefd = closefd
        self.fd = None
        self.size = None
        self.pos = 0
        self.offset = 0
        self.path = None
        self.bucket = None
        self.key = None
        self.client = None
        self.buffer = None
        self.buffer_size = 4096
        self.buffer_pos = 0
        self.buffer_len = 0
        self.buffer_fill = 1
        self.buffer_dirty = False

        if mode in 'wxa':
            self.fd = io.BytesIO()
            self.size = 0
        else:
            self.fd = None
            self.size = None

        if mode in 'r+wa':
            self.fd = None
            self.size = None

            if mode == 'r':
                self.buffer_fill = 0

            if self.size is None:
                self.size = int(self
