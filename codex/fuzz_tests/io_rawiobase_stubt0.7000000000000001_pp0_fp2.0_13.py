import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self._io = io.open(filename, mode)
        self._mode = mode
    def read(self, size=-1):
        return self._io.read(size)
    def write(self, data):
        self._io.write(data)
    def close(self):
        self._io.close()
    @classmethod
    def open(cls, filename, mode):
        return cls(filename, mode)
File.open('test.txt', 'w+').write('test')
File('test.txt', 'r').read()

# Почему не работает через метод __new__?
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self._io = io.open(filename, mode)
        self._mode = mode
    def read(self, size=-1):
        return self._io.read(size)
   
