import mmap
# Test mmap.mmap()

class MemMap:
    _map = None

    def __init__(self, filename):
        self._map = mmap.mmap(-1, 1024, mmap.MAP_ANON | mmap.MAP_SHARED)
        fd = os.open(filename, os.O_RDONLY)
        os.write(self._map.fileno(), os.read(fd, 1024))
        os.close(fd)

    def __del__(self):
        self._map.close()

    def get(self):
        return self._map

data = MemMap('test.txt')
m = data.get()

