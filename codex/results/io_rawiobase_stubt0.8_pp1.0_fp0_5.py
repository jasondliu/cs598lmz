import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self._pos = 0

    def read(self, length=None):
        self.file.seek(self._pos)
        data = self.file.read(length)
        self._pos = self.file.tell()
        return data

    def seekable(self):
        return True

    def seek(self, pos, where=io.SEEK_SET):
        if where == io.SEEK_SET:
            self._pos = pos
        elif where == io.SEEK_END:
            self._pos = self.file.get_length() + pos
        elif where == io.SEEK_CUR:
            self._pos += pos
        else:
            raise ValueError('where')

    def tell(self):
        return self._pos


async def aio_read(file: File, length: int):
    return await loop.run_in_executor(None, file.read, length)
    # return await asyncio.wait_for(file.read(length
