import io
# Test io.RawIOBase
class MyFileIO(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.raw = open(filename, mode)
        self.buffer = b''

    def read(self, count=-1):
        print(f'{self.filename}[read]({count})')
        if count == -1:
            count = len(self.buffer)
        if count <= len(self.buffer):
            print(f'\tReturning {count} bytes from buffer')
            out = self.buffer[:count]
            self.buffer = self.buffer[count:]
            return out
        else:
            out = self.buffer
            count -= len(self.buffer)
            self.buffer = b''
            while count > 0:
                data = self.raw.read(count)
                if not data:
                    break
                out += data
                count -= len(data)
            return out

