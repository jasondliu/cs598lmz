import io
class File(io.RawIOBase):
    def __init__(self,filed):
        self.filed=filed
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self,b):
        data=self.filed.read()
        n=len(data)
        b[:n]=data
        return n
    def write(self,b):
        return self.filed.write(b)
    def seek(self,offset,whence=0):
        return self.filed.seek(offset,whence)
    def tell(self):
        return self.filed.tell()
    def close(self):
        return self.filed.close()

def main():
    f=open("test.txt","a+")
    f=File(f)
    f.write("hello world\n")
    f.seek(0)
    print(f.read())
if __name__=='__main__':
    main()
