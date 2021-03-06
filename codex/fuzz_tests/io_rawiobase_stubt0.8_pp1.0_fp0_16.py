import io
class File(io.RawIOBase):
    def flush(self):
        pass
    def write(self,b):
        return super().write(b)
    def read(self,n=-1):
        return super().read(n)
    def readall(self):
        return super().read()
    def readable(self):
        return super().readable()
    def writable(self):
        return super().writable()
    def seekable(self):
        return super().seekable()
    def readline(self,limit=-1):
        return super().readline(limit)
    def readlines(self,hint=-1):
        return super().readlines(hint)
    def writeable(self):
        return super().writable()
    def writelines(self,lines):
        return super().writelines(lines)
    def tell(self):
        return super().tell()
    def close(self):
        return super().close()
    def seek(self,offset,whence=0):
        return super().seek(offset,whence)
    def fileno(self):
        return
