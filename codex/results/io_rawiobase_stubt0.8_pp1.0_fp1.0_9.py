import io
class File(io.RawIOBase):
    def __init__(self):
        self.data = b'Hello world'
        self.pos = 0
    def read(self, size):
        data = self.data[self.pos:self.pos+size]
        self.pos += len(data)
        return data
    def seekable(self):
        return True
    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = pos
        elif whence == io.SEEK_CUR:
            self.pos += pos
        else:
            raise ValueError(whence)
    def tell(self):
        return self.pos


oldstdin = sys.stdin
oldstdout = sys.stdout
oldsterr = sys.stderr
try:
    fin = File()
    fout = File()
    ferr = File()
    sys.stdin = fin
    sys.stdout = fout
    sys.stderr = ferr
    fout.write(b'Hello world!')
