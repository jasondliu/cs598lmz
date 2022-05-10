import mmap

class FileDescriptor(object):
    def __init__(self, fd):
        self.fd = fd

    def __repr__(self):
        return "<FileDescriptor %d>" % self.fd

    def close(self):
        os.close(self.fd)

    def fileno(self):
        return self.fd

class File(object):
    def __init__(self, file_):
        if isinstance(file_, str):
            file_ = file(file_, "r")
        self.file_ = file_
        self.fd = FileDescriptor(file_.fileno())
        self.size = os.fstat(self.fd.fileno()).st_size
        self.pos = 0
        self.readsize = 64 * 1024 * 1024

    def __repr__(self):
        return "<File %s>" % self.file_

    def read(self, size=None):
        if size is None:
            size = self.size

