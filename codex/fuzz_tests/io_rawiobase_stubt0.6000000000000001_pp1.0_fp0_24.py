import io
class File(io.RawIOBase):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def open_file(self):
        self.file = open(self.file_name, self.file_mode)

    def read(self):
        self.open_file()
        data = self.file.read()
        self.file.close()
        return data

    def write(self, data):
        self.open_file()
        self.file.write(data)
        self.file.close()

    def read_binary(self):
        self.open_file()
        data = self.file.read()
        self.file.close()
        return data

    def write_binary(self, data):
        self.open_file()
        self.file.write(data)
        self.file.close()

class DataReader(File):
    def __init__(self, file_name):
        super().__init__(file_name, 'r')

    def read
