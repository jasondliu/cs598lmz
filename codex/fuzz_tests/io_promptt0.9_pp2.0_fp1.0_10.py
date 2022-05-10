import io
# Test io.RawIOBase 
class FileIO(io.IOBase):

    def __init__(self, file, mode='r'):
        if mode not in ('r', 'w'):
            raise ValueError("mode must be 'r' or 'w'")
        self.mode = mode
        # here open() is where the file actually gets opened
        self._file = io.FileIO(file, mode)

    def read(self, n=-1):
        print self.closed
        print 'N value is ',n
        return self._file.read(n)

    def write(self, b):
        return self._file.write(b)


    def close(self):
        print 'Closing File Object...'
        if not self.closed:
            self._file.close()
        super(FileIO, self).close()
def main():
    f = FileIO("fileB.txt", "w")
    f.write('foobar')
    f.flush()
    f.seek(0)
    f.read()
    f.close()

if __name__ ==
