import io
class File(io.RawIOBase):
    def __init__(self, file_name):
        self.file = io.open(file_name, mode='r', encoding='utf-8')
        self.pos = 0
        self.size = os.path.getsize(file_name)
    def tell(self):
        return self.pos
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = self.size + pos
        else:
            raise 'Illegal whence={}'.format(whence)
    def readable(self):
        return True
    def read(self, n=None):
        line = self.file.readline()
        if len(line) == 0:
            return ''
        self.pos += len(line)
        return line
class FileBuffer:
    def __init__(self, file, max_size=1024, max_line_size=0):
        self.file = file
        self.
