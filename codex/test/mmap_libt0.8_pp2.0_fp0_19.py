import mmap

def create_file(filename, data):
    file = open(filename, "w+b")
    file.write(data)
    file.close()

def read_file(filename):
    file = open(filename, "r+b")
    mm = mmap.mmap(file.fileno(), 0)
