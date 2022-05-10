import io
class File(io.RawIOBase):
    _fd = os.open("C:/Users/donghyeon_cho/Desktop/송도 휴게소 게이트.mp4", os.O_RDONLY)
    def read(self,n= -1):
        if not self._closed:
            if n &gt;= 0:
                return os.read(self._fd, n)
            return os.read(self._fd, 1000000)

    def close(self):
        if not self._closed:
            os.close(self._fd)
            self._closed = True

f = File()
f.close()

```
</code>

