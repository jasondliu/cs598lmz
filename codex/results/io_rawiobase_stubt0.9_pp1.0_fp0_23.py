import io
class File(io.RawIOBase):
    def __init__(self, address, mode):
        self.address = address
        self.mode = mode
        self.file = open(self.address, self.mode)

    def read(self):
        data = self.file.read()
        return data

    def close(self):
        return self.file.close()


if __name__ == '__main__':
    with File('./py/python_2/read_me.md', 'rb') as f:
        print(f.read())
        f.close()
