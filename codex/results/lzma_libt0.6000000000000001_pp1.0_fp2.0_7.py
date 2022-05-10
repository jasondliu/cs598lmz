import lzma
lzma_path = './'

class FileObject:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = lzma.open(self.path, 'rt')
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

class LZMAFile(FileObject):
    def __init__(self, filename, mode='r'):
        self.path = filename
        self.file = None
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

import os
import lzma
class LZMA:
    def __init__(self, file_name):
        self.file_name = file_name

    def open(self, mode='r'):
        if mode == 'r':
            return l
