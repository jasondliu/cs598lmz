import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.pos = 0
        self.maxpos = 0
        self.data = None
        if 'r' in mode:
            self.data = self._read(path)
            self.maxpos = len(self.data)
        elif 'w' in mode:
            self.data = bytearray()
        elif 'x' in mode:
            if path in self.files:
                raise FileExistsError
            self.data = bytearray()
        elif 'a' in mode:
            self.data = self._read(path)
            self.maxpos = len(self.data)
            self.pos = self.maxpos

    @staticmethod
    def _read(path):
        return bytearray()

    def close(self):
        if 'w' in self.mode or 'a' in self.mode:
            self.files[self.path] = self.data
        self.data = None
       
