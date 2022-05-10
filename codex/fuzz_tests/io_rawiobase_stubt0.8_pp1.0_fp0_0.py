import io
class File(io.RawIOBase):
    def read(self, size= -1):
        return self.buffer


class CachedFile(File):
    def __init__(self, path):
        self.buffer = None
        self.opened = False
        self.path = path

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def open(self):
        if not self.opened:
            self.buffer = open(self.path, "rb").read()
            self.opened = True

    def close(self):
        if self.opened:
            self.buffer = None
            self.opened = False

class GridFile(File):
    def __init__(self, chunk_size, app, fs, grid_id):
        self.chunk_size = chunk_size
        self.app = app
        self.fs = fs
        self.grid_id = grid_id
        self.buffer = None
        self.opened = False
        self.pos = 0

    def __enter__
