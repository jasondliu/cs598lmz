import mmap

class File(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_size = os.stat(self.file_path).st_size

    def get_size(self):
        return self.file_size

    def get_content(self):
        f = open(self.file_path, 'r+b')
        mm = mmap.mmap(f.fileno(), 0)
        return mm.read(self.file_size)

    def __str__(self):
        return self.file_path
