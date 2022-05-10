import io
class File(io.RawIOBase):
    def write(self, data):
        raise NotImplementedError()

f = File()

f.write('hello')
