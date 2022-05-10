import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.mode = mode
        self.last_seek = 0
        self.close()

    def close(self):
        self.data = None

    def seek(self, position):
        self.last_seek = position
        return position

    def read(self, count):
        self.last_seek += count
        return self.data[self.last_seek - count:self.last_seek]

    def seekable(self):
        return self.mode.find('r') >= 0

    def readable(self):
        return self.mode.find('r') >= 0

    def writeable(self):
        return self.mode.find('w') >= 0

    def writelines(self, lines):
        if self.mode.find('w') >= 0:
            for line in lines:
                self.write(line)
            return len(lines)

#import collections

#class Namespace(collections.MutableMapping):
#    def __init__(self, trans=None, parent
