import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = open(file, 'r')
    def read(self, n = -1):
        return self.file.read()
class ReadFile:
    def __init__(self, file):
        self.file_obj = File(file)
    def read(self):
        return self.file_obj.read()
read_file = ReadFile('test.txt')
print(read_file.read())
#####

######
import re
class ReadFile:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.f_contents = self.file.read()
        num_lines = len(self.f_contents.splitlines())
        self.num_words = len(self.f_contents.split())
        non_space = re.compile(r'\S')
        white_spaces = self.f_contents.split(non_space)
        self.num_whitespaces = len(white_spaces)
