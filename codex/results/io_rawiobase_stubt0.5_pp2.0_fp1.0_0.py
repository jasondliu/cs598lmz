import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            r = self.file.readinto(view)
            view = view[r:]
            n -= r
            if r == 0:
                break
        return len(b) - n
class Stream(io.RawIOBase):
    def __init__(self, stream):
        self.stream = stream
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            r = self.stream.readinto(view)
            view = view[r:]
            n -= r
            if r == 0:
                break
        return len(b) - n

class StreamReader(io.BufferedReader):
    def __init__(self, stream):
        self.stream = stream
        self.raw = Stream(stream)
        super().
