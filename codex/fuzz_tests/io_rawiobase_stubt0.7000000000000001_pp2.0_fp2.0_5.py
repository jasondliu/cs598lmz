import io
class File(io.RawIOBase):
    def __init__(self, file, cache_size=None):
        self.file = file
        self.name = file.name
        self.mode = file.mode
        self.cache_size = cache_size
        if cache_size is not None:
            self.cache = io.BytesIO()
        else:
            self.cache = None
        self.closed = False
        self.cached_pos = 0

    def readable(self):
        return self.file.readable()

    def writable(self):
        if self.mode == 'w':
            return True
        return False

    def seekable(self):
        return True

    def read(self, *args):
        if self.cache is None:
            return self.file.read(*args)
        #print('read', self.cached_pos, self.tell(), args)
        if self.cached_pos > self.tell():
            self.cache.seek(0, io.SEEK_SET)
            self.cached_pos = 0
        while self.cached_pos
