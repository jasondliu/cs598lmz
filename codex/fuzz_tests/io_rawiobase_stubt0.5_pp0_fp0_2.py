import io
class File(io.RawIOBase):
    def __init__(self,name):
        self.name = name
    def read(self,size = -1):
        print('read')
        return b'123'
    def readinto(self,b):
        print('readinto')
        return b'123'
    def readall(self):
        print('readall')
        return b'123'
    def seek(self,offset,whence = 0):
        print('seek')
    def tell(self):
        print('tell')
    def truncate(self,size = None):
        print('truncate')
    def write(self,b):
        print('write')
    def writelines(self,lines):
        print('writelines')

f = File('/tmp/test.txt')
f.read()
f.readinto(b'123')
f.readall()
f.seek(1)
f.tell()
f.truncate()
f.write(b'123')
f.writelines(b'123')
