import io
class File(io.RawIOBase):
    def __init__(self, name: str):
        self.file = open(name, 'rb')

    def write(self, b: bytes) -> int:
        self.seek(0, 2)
        return self.file.write(b)

    def read(self, n: int = None) -> bytes:
        return self.file.read(n)

    def readable(self) -> bool:
        return True

    def writable(self) -> True:
        return True

    def seekable(self) -> True:
        return True

    def seek(self, pos: int, (-1, 0, 1)) -> int:
        return self.file.seek(pos, whence)

    def tell(self) -> int:
        return self.file.tell()

    def flush(self) -> None:
        self.file.flush()

    def close(self) -> None:
        self.file.close()

def main():
    f = File('test.py')
    f.write(b'0123456789')
    f.seek(
