import io
class File(io.RawIOBase):
    def __init__(self, path: str, mode: str = 'r'):
        self.path = path
        self.mode = mode
        self.file = open(path, mode)

    def read(self, size: int = -1) -> bytes:
        return self.file.read(size)

    def readinto(self, b: bytearray) -> int:
        return self.file.readinto(b)

    def write(self, b: bytes) -> int:
        return self.file.write(b)

    def seek(self, offset: int, whence: int = 0) -> int:
        return self.file.seek(offset, whence)

    def close(self) -> None:
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
