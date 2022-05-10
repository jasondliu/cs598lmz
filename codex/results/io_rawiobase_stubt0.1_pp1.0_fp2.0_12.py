import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

def open(file, mode="r"):
    if mode not in ("r", "rb"):
        raise NotImplementedError("only read binary mode is supported")
    return File(file)

def main():
    import sys
    import wave
    import contextlib
    with contextlib.closing(wave.open(open(sys.argv[1], "rb"))) as f:
        print("channels:", f.getnchannels())
        print("sample width:", f.getsamp
