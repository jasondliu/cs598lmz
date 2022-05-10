import io
class File(io.RawIOBase):
    def read(self, n=0):
        print("f.read()")
        print(n)
        pass
    def write(self, buf):
        print("f.write()")
        pass
    def flush(self):
        print("f.flush()")
        pass
    def seek(self, offset, whence=0):
        print("f.seek()")
        pass
    def fileno(self):
        print("f.filen()")
        pass

f = File()
f.seek(1,2)
