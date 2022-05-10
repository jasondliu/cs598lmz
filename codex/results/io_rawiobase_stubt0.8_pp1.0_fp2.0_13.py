import io
class File(io.RawIOBase):
    def __init__(self, next_file):
        self.next_file = next_file
        self.position = 0

    def read(self, size=-1):
        if size == -1:
            data = self.next_file[self.position:]
            self.position = len(self.next_file)
            return data

        if self.position + size &gt; len(self.next_file):
            size = len(self.next_file) - self.position
        data = self.next_file[self.position:self.position + size]
        self.position += size
        return data

    def readline(self, size=-1):
        # Read until newline or EOF
    def seek(self, offset, whence=0):
        if whence == os.SEEK_SET:
            self.position = offset
        elif whence == os.SEEK_CUR:
            self.position += offset
        elif whence == os.SEEK_END:
            self.position = len(self.next_file) - offset
    def tell
