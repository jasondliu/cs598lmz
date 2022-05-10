import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FileIO(io.FileIO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BytesIO(io.BytesIO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class StringIO(io.StringIO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
