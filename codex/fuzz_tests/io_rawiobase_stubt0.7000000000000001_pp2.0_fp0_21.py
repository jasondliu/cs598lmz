import io
class File(io.RawIOBase):
    def __init__(self,filename,mode):
        self.file=open(filename,mode)
    def read(self,size=-1):
        return self.file.read(size)
    def write(self,b):
        return self.file.write(b)
    def close(self):
        return self.file.close()
    @classmethod
    def open(cls,filename,mode):
        return cls(filename,mode)

def test_file():
    filename=r'c:\temp\mytest.txt'
    f=File.open(filename,'w+')
    f.write('hello world')
    f.write('hello world')
    f.write('hello world')
    f.seek(0)
    print(f.read())
    f.close()


if __name__ == '__main__':
    test_file()
