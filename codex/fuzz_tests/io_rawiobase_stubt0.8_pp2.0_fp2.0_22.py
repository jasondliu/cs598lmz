import io
class File(io.RawIOBase):
    def __init__(self, f, length):
        self.f = f
        self.length = length
        self.offset = 0
        self.f = io.BytesIO(f.read(length))

    def close(self):
        self.f.close()

    def readinto(self, b):
        read_size = len(b)
        if self.offset + read_size &gt; self.length:
            if self.offset &gt;= self.length:
                return 0
            read_size = self.length - self.offset

        view = memoryview(b)
        result = self.f.readinto(view[:read_size])
        self.offset += read_size
        return read_size

    def readable(self):
        return True

with open("archive.zip", "rb") as f:
    archive = zipfile.ZipFile(f)
    for info in archive.infolist():
        if not info.is_dir():
            content = archive.read(info)
            newfile = File(io.BytesIO
