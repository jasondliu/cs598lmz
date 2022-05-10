import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path

    def read(self, size=-1):
        with open(self.path, 'rb') as f:
            return f.read(size)

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True


def get_file_from_path(path):
    return File(path)


def get_file_from_request(request):
    return request.file


def get_file_from_stream(stream):
    return stream


def get_file_from_bytes(bytes):
    class BytesIO(io.BytesIO):
        def __init__(self, buf):
            io.BytesIO.__init__(self)
            self.write(buf)
            self.seek(0)

    return BytesIO(bytes)


def get_file_from_url(url):
    return get_file_from_path(url)
