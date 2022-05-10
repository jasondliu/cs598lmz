import io
class File(io.RawIOBase):
    def __init__(self, f: io.RawIOBase, out: io.RawIOBase):
        self.f = f
        self.out = out
        self.file_name = ''

    def read(self, n=-1):
        cnt = n
        while True:
            if cnt > 0:
                cnt -= 1
                b = self.f.read(1)
            else:
                b = self.f.read(1)
            if b == b'\x1B':
                for i in range(3):
                    self.f.read(1)
                self.file_name = self.f.read(1024).decode('utf-8').split('\x00')[0]
                print('file name', self.file_name)
                self.out.write(b'\x7E')
                self.out.write(self.file_name.encode('utf-8'))
                self.out.write(b'\x1B')
            elif b == b'\x7E':
                self
