import io
class File(io.RawIOBase):
    """Mock file."""
    def readable(self):
        return True

    def __init__(self, data, name="test.xml"):
        self.data = data
        self.closed = False
        self.name = name

    def read(self, size=-1):
        if size == -1:
            size = len(self.data)
        ret = self.data[:size]
        self.data = self.data[size:]
        return ret

    def readline(self):
        ret = self.data.parts[0]
        self.data = str(self.data)[len(ret):]
        return ret


class XMLCulture(Culture):
    def read_book(self, path, verbose=False):
        with open(path, 'r') as f:
            data = f.read()
        file = File(data, name=path)
        # file = open(path, 'r')
        book = self.read_book_file(file)
        file.close()
        return book

    def read_
