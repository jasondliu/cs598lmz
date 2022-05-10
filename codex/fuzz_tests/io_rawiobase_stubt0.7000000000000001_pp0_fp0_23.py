import io
class File(io.RawIOBase):
    def __init__(self, file_path, write=False):
        self.file_path = file_path
        self.write = write
        self.opened = False
        self.file = None
        self.current_pos = 0
        self.size = 0

    def write(self, b):
        self.file.write(b)
        self.size += len(b)

    def seekable(self):
        return True

    def readable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            if offset < self.size:
                self.current_pos = offset
                self.file.seek(offset)
            else:
                raise Exception("Unable to seek this far")
        elif whence == io.SEEK_CUR:
            if offset + self.current_pos < self.size:
                self.current_pos += offset
                self.file.seek(offset, whence)
            else:
                raise Exception("Unable to seek this far
