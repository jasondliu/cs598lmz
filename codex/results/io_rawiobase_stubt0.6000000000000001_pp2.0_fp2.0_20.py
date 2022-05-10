import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.f = open(name, mode)
        self.f.seek(0)

    def read(self, size=-1):
        if size == -1:
            size = self.f.seek(0, 2)
        self.f.seek(0)
        return self.f.read(size)

    def close(self):
        self.f.close()

def file(name, mode):
    return File(name, mode)

def main():
    with open("/home/kamei/workspace/dataset/voc/voc2012.tar.gz", "rb") as f:
        print(f.read())

    with file("/home/kamei/workspace/dataset/voc/voc2012.tar.gz", "r") as f:
        print(f.read())

if __name__ == '__main__':
    main()
