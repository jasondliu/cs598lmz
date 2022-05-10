import io
class File(io.RawIOBase):
    def __init__(self,filename,mode):
        self._file=open(filename,mode)
    def close(self):
        self._file.close()
    def fileno(self):
        return self._file.fileno()
    def readinto(self,b):
        return self._file.readinto(b)

f=File('/etc/passwd','r')
print f.read(5)
f.close()

class File2(io.RawIOBase):
    def __init__(self,file):
        self._file=file
    def close(self):
        self._file.close()
    @property
    def name(self):
        return self._file.name
    def fileno(self):
        return self._file.fileno()
    def readinto(self,b):
        return self._file.readinto(b)

f=File2(open('/etc/passwd','r'))
print f.read(15)
print f.name
f.close()

class File3(io.Raw
