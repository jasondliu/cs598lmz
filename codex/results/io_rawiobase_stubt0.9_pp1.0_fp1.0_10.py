import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', create=False):
        self.file = io.BytesIO()
        self.path = path
        self.mode = mode
        self.create = create
        self.pos = 0
        if 'r' in mode:
            self.file_mode = 'rb'
            self.open = self.read_open
        elif '+' in mode:
            self.file_mode = 'r+b'
            self.open = self.read_write_open
        else:
            self.file_mode = 'wb'
            self.open = self.write_open
        entire_file = self.open()
        if entire_file:
            if 'b' in self.mode:
                self.file.write(entire_file)
            else:
                self.file.write(entire_file.encode('utf-8'))
        else:
            if create:
                self.write(b'')

    def write_open(self):
        try:
            with open(self.path
