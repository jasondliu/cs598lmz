import io
class File(io.RawIOBase):
    def __init__(self, file, mode='rb', closefd=True):
        return super(File, self).__init__()


class StringIO(io.StringIO):
    def __init__(self, file, mode='rb', closefd=True):
        return super(StringIO, self).__init__()


class BytesIO(io.BytesIO):
    def __init__(self, file, mode='rb', closefd=True):
        return super(BytesIO, self).__init__()
