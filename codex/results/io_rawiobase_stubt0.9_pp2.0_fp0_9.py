import io
class File(io.RawIOBase):
    def __init__(self, name: str, mode: str) -> None:
        self.name = name
        self.mode = mode

    def __enter__(self) -> io.RawIOBase:
        self.file = io.FileIO(self.name, self.mode)
        return self

    def __exit__(self, type, value, traceback) -> None:
        if not self.closed:
            self.close()

    def read(self, size:-1) -> bytes:
        value = self.file.read(size)
        print(f'read({size}) -> {value!r}')
        return value

    def write(self, b: bytes) -> int:
        value = self.file.write(b)
        print(f'write({b!r}) -> {value!r}')
        return value

    def readable(self) -> bool:
        return True

    def writable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return True

    def seek(self, offset: int
