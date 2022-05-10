import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode='r'):
        self.file_obj = open(file_name, mode)
        self.file_name = file_name
        self.mode = mode
        self.buffer = ''
        self.buffer_size = 0
        self.buffer_pos = 0
        self.buffer_len = 0
        self.file_pos = 0
        self.file_size = 0
        self.file_len = 0
        self.read_size = 0
        self.read_pos = 0
        self.read_len = 0
        self.read_buffer = ''
        self.read_buffer_size = 0
        self.read_buffer_pos = 0
        self.read_buffer_len = 0
        self.read_file_pos = 0
        self.read_file_size = 0
        self.read_file_len = 0
        self.read_size_pos = 0
        self.read_size_size = 0
        self.read_size_len = 0
        self.read_size_
