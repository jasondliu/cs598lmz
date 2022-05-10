import io
class File(io.RawIOBase):
    def read(self, size=None):
        if size == None:
            print("mode is Data-Size")
        else:
            print("mode is Data-Byte")
        print("size number is: %s" % str(size))

    def write(self, size):
        print("Mode is write")
        print("size number is: %s" % str(size))

    def fileno():
        print("mode is file number")

    def seek():
        print("mode is seek")

    def close():
        print("mode is close")

"""
class IOStream(File):
    def __init__(self, file)
        File.__init__(self,file)
        self.file_object=file
    def read(self):
        return File.read(self)

    def write(self,buffer):
        return File.write(self)
    def close(self):
        self.file_object.close()
        return File.close(self)
"""


class IOStream:
    def __init__(self, file):
        self
