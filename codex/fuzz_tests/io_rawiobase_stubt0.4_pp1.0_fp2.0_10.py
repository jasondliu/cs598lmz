import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = open(name, "rb")
        self.pos = 0
        self.size = os.path.getsize(name)

    def read(self, size=-1):
        if size == -1:
            return self.f.read()
        else:
            return self.f.read(size)

    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.size + offset
        else:
            raise ValueError("Invalid whence")
        self.f.seek(self.pos)

    def tell(self):
        return self.pos

    def close(self):
        self.f.close()

    def __repr__(self):
        return "<File %s>" % self.name


class FileSystem(object):
    def __init__(self, root):
        self.root
