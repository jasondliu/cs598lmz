import io
class File(io.RawIOBase):
    ...
    def fileno(self) -> int:
        ...
    def seekable(self) -> bool:
        ...
    def seek(self, pos: int, whence: int = os.SEEK_SET) -> int:
        ...
    def readable(self) -> bool:
        ...
    def readinto(self, b: 'bytearray') -> int:
        ...
    def writeable(self) -> bool:
        ...
    def write(self, b: 'bytes') -> int:
        ...
class IOBase(RawIOBase):
    ...
    def seekable(self) -> bool:
        ...
class StringIO(IOBase):
    ...
    def write(self, s: str) -> int:
        ...
def isatty(f: IO[str]) -> bool:
    ...
class TextIOWrapper(TextIOBase):
    ...
    def write(self, s: str) -> int:
        ...
class BufferedIOBase(IOBase):
    ...
    def detach(self) -> file:
       
