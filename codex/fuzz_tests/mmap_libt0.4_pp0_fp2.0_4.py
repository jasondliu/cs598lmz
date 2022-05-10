import mmap

def get_size(filename):
    st = os.stat(filename)
    return st.st_size

def get_file_contents(filename):
    with open(filename, 'r') as f:
        return f.read()

def get_file_contents_mmap(filename):
    f = open(filename, 'r')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    return s

def get_file_contents_mmap_size(filename):
    f = open(filename, 'r')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    return len(s)

def get_file_contents_mmap_size_2(filename):
    f = open(filename, 'r')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    return s.size()

def get_file_contents_mmap_
