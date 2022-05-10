import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
        self.file_size = None
        self.file_size_read = 0
        self.buffer_size = 1024
        self.buffer = None
        self.buffer_read_index = 0
        self.buffer_size_read = 0
        self.buffer_size_read_index = 0
        self.buffer_size_read_index_previous = 0
        self.buffer_size_read_index_previous_previous = 0
        self.buffer_size_read_index_previous_previous_previous = 0
        self.buffer_size_read_index_previous_previous_previous_previous = 0
        self.buffer_size_read_index_previous_previous_previous_previous_previous = 0
        self.buffer_size_read_index_previous_previous_previous_previous_previous_previous = 0
        self.buffer_size_read_index_pre
