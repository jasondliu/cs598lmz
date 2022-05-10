import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def read(self, n=-1):
        self.file.seek(self.offset)
        s = self.file.read(n)
        self.offset += len(s)
        return s

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.size
        self.offset = offset
        return self.offset

    def tell(self):
        return self.offset

def get_file_from_url(url):
    response = requests.get(url, stream=True)
    return File(response.raw)

def get_file_from_path(path):
    return open(path, 'rb')

def get_file(file):
    if file.startswith('http'):
        return get
