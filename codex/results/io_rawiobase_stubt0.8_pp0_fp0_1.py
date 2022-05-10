import io
class File(io.RawIOBase):
    def get_content(self):
        return self.read()

# http://www.voidspace.org.uk/python/mock/examples.html
try:
    from unittest import mock
except ImportError:
    import mock

class FileInMemory(File):
    def __init__(self, file_info):
        self.file_info = file_info
        self._mock_stream = io.StringIO()
    def get_content(self):
        self._mock_stream.seek(0)
        return self._mock_stream.read()

class FileOnDisk(File):
    def __init__(self, file_info):
        self.file_info = file_info
        self.path = file_info.get_file_path()
    def read(self):
        with open(self.path, 'rb') as f:
            return f.read()
    def write(self, data):
        with open(self.path, 'wb') as f:
            return f.write(data)

class FileM
