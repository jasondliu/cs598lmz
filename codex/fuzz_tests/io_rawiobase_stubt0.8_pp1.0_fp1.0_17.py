import io
class File(io.RawIOBase):
    def read(self):
        print('raw.read')
        return 'abc'

    def write(self, data):
        print('raw.write')
        return len(data)

    def readable(self):
        return True

class Text(File):
    def read(self):
        print('Text.read')
        return super().read().split('\n')

    def write(self, data):
        print('Text.write')
        return super().write('\n'.join(data))

    def writable(self):
        return True

#f = Text()
#print(f.read())
#print(f.write(['asd']))

class FixedWidth:
    def __init__(self, width, names, types):
        self.width = width
        self.names = names
        self.types = types

    def get_line(self, line):
        values = line[:self.width]
        line = line[self.width:]
        return line, [f(s) for f, s in zip(self.types,
