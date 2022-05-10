import io
class File(io.RawIOBase):
    def __init__(self, fp):
        self._fp = fp

    def readinto(self, b):
        return self._fp.readinto(b)

    def write(self, b):
        return self._fp.write(b)

    def readable(self):
        return True

    def writable(self):
        return True

class BlockDev(BlockDevBase):
    def __init__(self, dev):
        self._dev = dev

    def get_size(self):
        return os.stat(self._dev).st_size

    def open(self, mode):
        return File(open(self._dev, mode))

class DiskDev(BlockDev):
    def __init__(self, dev):
        super().__init__(dev)
        self._dev = dev

    def get_size(self):
        return self._get_size(self._dev)

    @staticmethod
    def _get_size(dev):
        with open(dev, "rb") as fp:
            fp.seek(0, io
