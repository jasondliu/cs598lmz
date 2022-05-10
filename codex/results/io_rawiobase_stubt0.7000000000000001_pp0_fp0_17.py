import io
class File(io.RawIOBase):

    def __init__(self, file):
        self.file = file

    def read(self, n=-1):
        return self.file.read(n)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()


class StringIO(io.BytesIO):

    def seekable(self):
        return True


class StringIOWithFile(File, StringIO):

    def __init__(self, file):
        StringIO.__init__(self, file.read())
        self.file = file


def _file_type(file):
    if isinstance(file, io.RawIOBase):
        return File(file)
    elif isinstance(file, io.BufferedIOBase):
        return file
    elif isinstance(file, io.BytesIO):
        return StringIOWithFile(file)
    else
