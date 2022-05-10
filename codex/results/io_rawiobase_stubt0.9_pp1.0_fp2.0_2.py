import io
class File(io.RawIOBase):
        def __init__(self, hService, hFile):
                super().__init__()
                self.hService = hService
                self.hFile = hFile
        def read(self, size=-1) -> bytes:
                if size < 0:
                        value = None
                elif size == 0:
                        return b''
                elif size > 0x100000000:
                        raise OverflowError
                else:
                        value = size
                res = readFile(self.hService, self.hFile, value)
                if res is None:
                        raise EOFError
                else:
                        return res
        def seek(self, offset: int, whence: int=io.SEEK_SET) -> int:
                return seekFile(self.hService, self.hFile, offset, whence)
        def write(self, data: bytes) -> int:
                writeFile(self.hService, self.hFile, data, len(data))
                return len(data)

class Directory(io.RawIOBase):
        def __init__(self, hService,
