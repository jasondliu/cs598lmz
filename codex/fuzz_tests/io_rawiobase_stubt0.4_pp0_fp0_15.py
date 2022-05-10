import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readable(self):
        return True
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

def read_data(file):
    file = File(file)
    return file.read(10)

def read_data_2(file):
    file = File(file)
    return file.read(10)

def read_data_3(file):
    file = File(file)
    return file.read(10)

def read_data_4(file):
    file = File(file)
    return file.read(10)

def read_data_5(file):
    file = File(file)
    return file
