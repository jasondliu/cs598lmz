import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd

    def writable(self):
        return False

    def readable(self):
        return True

    def seekable(self):
        return False

    deffileno = lambda s: s.fd.fileno

    def readinto(self, buffer):
        return self.fd.readinto(buffer)


class Iter:
    def __init__(self, iterable):
        self.iter = iterable

    def __next__(self):
        x = next(self.iter)
        return x

    def __iter__(self):
        return self


class Dict(dict):
    def __missing__(self, k):
        return None


class List(list):
    def __getitem__(self, index):
        return None


class Task:
    def __init__(self, coro):
        self.coro = coro

    def send(self, value=None):
        try:
            return self.coro.send(value)
        except Stop
