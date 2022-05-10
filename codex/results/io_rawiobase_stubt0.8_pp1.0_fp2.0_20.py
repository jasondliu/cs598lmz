import io
class File(io.RawIOBase):
    """
    A container for data that resides on the native file system.
    """
    def __init__(self, root, relpath):
        self.root = root
        self.relpath = relpath

    @classmethod
    def from_path(cls, path):
        return cls.from_string(path.as_posix())

    @classmethod
    def from_string(cls, string):
        parts = string.split("/")
        root = parts[0]
        relpath = os.path.join(*parts[1:])
        return cls(root, relpath)

    def __repr__(self):
        return "File({}, {})".format(self.root, self.relpath)

    def open(self):
        return open(self.as_path(), "rb")

    def as_path(self):
        parts = [self.root] + self.relpath.split("/")
        return os.path.join(*parts)
    
    def as_string(self):
        return "/".join([self
