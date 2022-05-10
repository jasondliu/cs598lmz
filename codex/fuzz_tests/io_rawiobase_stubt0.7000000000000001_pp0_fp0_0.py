import io
class File(io.RawIOBase):
    def __init__(self, file_name, file_mode):
        self.closed = False
        self.file_name = file_name
        self.file_mode = file_mode
        if file_mode == 'rb':
            self.file = open_file(file_name, 'r', 'NXmx')
        elif file_mode == 'wb':
            self.file = open_file(file_name, 'w', 'NXmx')
        else:
            raise ValueError('Invalid file mode')
    def close(self):
        if not self.closed:
            self.file.close()
            self.closed = True
    def readable(self):
        return self.file_mode == 'rb'
    def writable(self):
        return self.file_mode == 'wb'
    def seek(self, offset, whence=0):
        if whence == 0:
            self.file.seek(offset)
        elif whence == 1:
            self.file.seek(self.file.tell() + offset)
        elif whence == 2
