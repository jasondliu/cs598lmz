import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
        self.file_size = 0
        self.file_size_read = 0
        self.file_offset = 0
        self.file_offset_read = 0
        self.file_offset_write = 0
        self.file_offset_read_end = 0
        self.file_offset_write_end = 0
        self.file_offset_read_end_size = 0
        self.file_offset_write_end_size = 0
        self.file_offset_read_end_size_total = 0
        self.file_offset_write_end_size_total = 0
        self.file_offset_read_end_size_total_max = 0
        self.file_offset_write_end_size_total_max = 0
        self.file_offset_read_end_size_total_max_set = 0
        self.file_offset_write_end_size_total_max_set = 0
        self.
