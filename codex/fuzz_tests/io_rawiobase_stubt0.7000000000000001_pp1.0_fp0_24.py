import io
class File(io.RawIOBase):
    def __init__(self):
        #super(File, self).__init__()
        self.name = "file"
        self.mode = "wb"
        self.closed = True


    def open(self, name, mode):
        self.name = name
        self.mode = mode

    def write(self, data):
        print(data)

    def read(self, size):
        pass

    def seek(self, offset, whence):
        pass

class CSVReader(File):
    def __init__(self):
        super(CSVReader, self).__init__()
        self.delimiter = ","
        self.fields = []

    def read(self, size):
        print("CSVReader")
        super(CSVReader, self).read(size)


class PDFReader(File):
    def __init__(self):
        super(PDFReader, self).__init__()
        self.page = 1

    def read(self, size):
        print("PDFReader")
        super(PDFReader, self).read
