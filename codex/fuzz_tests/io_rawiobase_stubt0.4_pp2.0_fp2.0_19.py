import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_obj = None
        self.current_offset = 0
        self.file_size = os.path.getsize(file_path)

    def read(self, size=-1):
        if self.file_obj is None:
            self.file_obj = open(self.file_path, 'rb')
            self.file_obj.seek(self.current_offset)
        data = self.file_obj.read(size)
        self.current_offset = self.file_obj.tell()
        return data

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.current_offset = offset
        elif whence == io.SEEK_CUR:
            self.current_offset += offset
        elif whence == io.SEEK_END:
            self.current_offset = self.file_size + offset
        else:
            raise ValueError("Invalid value for `
