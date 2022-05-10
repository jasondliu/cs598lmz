import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode='r+b'):
        self.file_object = open(file_path, mode)

    def close(self):
        self.file_object.close()
        self.file_object = None

    def __getattr__(self, item):
        return getattr(self.file_object, item)

    @property
    def name(self):
        return self.file_object.name

class FileIO(File, io.IOBase):
    def write(self, s):
        if isinstance(s, unicode):
            s = s.encode("utf-8")

        return self.file_object.write(s)

    def read(self, size=-1):
        return self.file_object.read(size)

def open(file_path, mode='r+b'):
    return FileIO(file_path, mode)

if __name__ == '__main__':
    with open('test.txt', 'w+') as f:
        f.write("你
