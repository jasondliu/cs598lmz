import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.fd = os.open(filename, os.O_RDONLY)
    def read(self, count=-1):
        return os.read(fd, count)
    def readinto(self, buf):
        return os.read(fd, len(buf))
    def close(self):
        os.close(self.fd)

f = File("test.py")
print(f.read())

# 从 tar 文件读取
import tarfile, io
tar = tarfile.open("mytarfile.tar")
for member in tar.getmembers():
    # only extract python source files
    if member.isfile() and member.name.endswith(".py"):
        fobj = tar.extractfile(member)
        # read the source file
        source = fobj.read()
        # do something with the source
        print(source)

# 从 zip 文件读取
import zipfile, io
zip
