import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        return self.f.close()

def pickle_dump(obj, file, protocol=None, *, fix_imports=True):
    if protocol is None:
        protocol = 3
    if not hasattr(file, "write"):
        raise TypeError("file must have a 'write' attribute")
    if not isinstance(file, (io.RawIOBase, File)):
        if fix_imports:
            return Pickler(file, protocol).dump(obj)
        else:
            return Unpickler(file).dump(obj)
    if fix_imports:
        return Pickler(file, protocol, fix_imports=True).dump(obj)
    else:
        return Unpickler(file, fix_imports=False).dump(obj)

def pick
