import io
class File(io.RawIOBase):
    def read(self, size, tag=None):
        raise NotImplementedError()
    def readinto(self, b, tag=None):
        raise NotImplementedError()
    def write(self, b, tag=None):
        raise NotImplementedError()
    def seek(self, offset, whence=0, tag=None):
        raise NotImplementedError()
    def tell(self, tag=None):
        raise NotImplementedError()
    def close(self):
        raise NotImplementedError()

class NamedFile(File):
    def __init__(self, name):
        super(File, self).__init__()
        self._name = name
    def name(self):
        return self._name
    def __repr__(self):
        return "NamedFile({0})".format(self._name)

class FuseFile(io.FileIO):
    def __init__(self, openfile, *args, **kargs):
        super(FuseFile, self).__init__(*args, **k
