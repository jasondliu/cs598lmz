import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.closed = True
        self.position = 0




    def open(self, mode='wb'):
        self.mode = mode
        self.pos = 0
        self.closed = False
        self.fileno = 1

    def close(self):
        pass

    def write(self, data):
        with open(self.name, 'ab+') as fd:
            if fd.tell() > 0:
                fd.seek(0, 2)
            fd.write(data)

    def read(self, size = -1):
        data = ''
        with open(self.name, 'rb') as fd:
            if fd.tell() >0:
                fd.seek(self.pos, 0)
                if size == -1:
                    data = fd.read()
                else:
                    data = fd.read(size)
                    self.pos+=size
        return data

    def seek(self, offset, whence=0):

