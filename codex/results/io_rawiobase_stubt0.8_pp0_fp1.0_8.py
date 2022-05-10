import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def close(self):
        try:
            self.f.close()
        except AttributeError:
            pass
    def read(self, n):
        try:
            return self.f.read(n)
        except:
            return b''
    def readinto(self, buf):
        try:
            return self.f.readinto(buf)
        except AttributeError:
            b = self.read(len(buf))
            n = len(b)
            try:
                buf[:n] = b
            except TypeError as e:
                import array
                if not isinstance(buf, array.array):
                    raise e
                buf[:n] = array.array('b', b)
            return n
    def seek(self, pos, whence=0):
        return self.f.seek(pos, whence)
    def write(self, b):
        try:
            return self.f.write(b)
        except AttributeError:
            return Not
