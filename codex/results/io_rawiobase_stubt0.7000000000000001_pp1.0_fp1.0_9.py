import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self._closed = False
        self._handle = open(self.name, 'rb')

    def read(self, size=-1):
        return self._handle.read(size)

    def close(self):
        if self._closed:
            return
        self._closed = True
        self._handle.close()

    def __del__(self):
        self.close()


def file_reader(name, chunk_size=1024):
    """
    generator function
    """
    try:
        f = File(name)
        while True:  # read by block of chunk_size
            data = f.read(chunk_size)
            if not data:
                break

            yield data
    finally:
        f.close()


if __name__ == '__main__':
    # read the entire file
    for chunk in file_reader('test.txt'):
        pass
