import io
class File(io.RawIOBase): pass
class Subfile(io.RawIOBase): pass
class FileProperty():
    fcntl = __import__('fcntl')
    def __get__(self, obj, type=None):
        return fcntl.fcntl(obj.fileno(), self.fcntl.F_GETFL)
    def __set__(self, obj, val):
        fcntl.fcntl(obj.fileno(), self.fcntl.F_SETFL, val)

if 'F_GETFL' in fcntl.__dict__:
    File.mode = FileProperty()
    Subfile.mode = FileProperty()

class BufferedWriter(Subfile):
    def __init__(self, file, buffer_size=io.DEFAULT_BUFFER_SIZE):
        if not isinstance(file, io.RawIOBase):
            raise TypeError("argument must be a IOBase")
        if not file.writable():
            raise io.UnsupportedOperation("underlying file must be writable")
        self.file = file
        self
