import mmap
import sys

class mmap_file():
    def __init__(self, fname, size, mode, offset=0):
        self.fname = fname
        self.size = size
        self.mode = mode
        self.offset = offset
        self.file_obj = open(fname, mode)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.file_obj.close()

    def __getitem__(self, key):
        self.file_obj.seek(self.offset + key)
        return self.file_obj.read(1)

    def __setitem__(self, key, value):
        self.file_obj.seek(self.offset + key)
        self.file_obj.write(value)

    def __len__(self):
        return self.size

