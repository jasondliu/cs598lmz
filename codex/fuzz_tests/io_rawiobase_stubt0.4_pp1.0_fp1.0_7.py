import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read()

class FileWrapper(object):
    def __init__(self, filelike):
        self.filelike = filelike
    def read(self, n=-1):
        return self.filelike.read()

class FileWrapper2(object):
    def __init__(self, filelike):
        self.filelike = filelike
    def read(self, n=-1):
        return self.filelike.read()
    def __getattr__(self, name):
        return getattr(self.filelike, name)

# test 1
# file = open('/tmp/test.txt', 'r')
# file = File(file)
# file = FileWrapper(file)
# file = FileWrapper2(file)
# print(file.read())

# test 2
# file = open('/tmp/test.txt', 'r')
# file = File(file)
# file
