import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
        self.file_size = 0
        self.file_pos = 0
        self.file_name = ""
        self.file_ext = ""
        self.file_name_ext = ""
        self.file_name_ext_size = 0
        self.file_name_ext_pos = 0
        self.file_name_ext_pos_end = 0
        self.file_name_ext_pos_end_size = 0
        self.file_name_ext_pos_end_pos = 0
        self.file_name_ext_pos_end_pos_size = 0
        self.file_name_ext_pos_end_pos_pos = 0
        self.file_name_ext_pos_end_pos_pos_size = 0
        self.file_name_ext_pos_end_pos_pos_pos = 0
        self.file_name_ext_pos_end_pos_pos_pos_size = 0
