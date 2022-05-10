import io
class File(io.RawIOBase):
    def __init__(self, f):
        self._f = f
    def read(self, n=-1):
        return self._f.read(n)
    def readable(self):
        return True

class StringIO(io.StringIO):
    def __init__(self, s):
        self._s = s
    def read(self):
        return self._s

class BytesIO(io.BytesIO):
    def __init__(self, b):
        self._b = b
    def read(self):
        return self._b

class TextIOWrapper(io.TextIOWrapper):
    def __init__(self, f):
        self._f = f
    def read(self):
        return self._f.read()

class BufferedReader(io.BufferedReader):
    def __init__(self, f):
        self._f = f
    def read(self):
        return self._f.read()

class BufferedWriter(io.BufferedWriter):
    def __init__(self,
