import mmap
# Test mmap.mmap
def read_mmap(filename):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDONLY)
    buf = mmap.mmap(fd, size, mmap.MAP_SHARED, mmap.PROT_READ)
    os.close(fd)
    return buf

# Test pickle
def read_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Test mmap.mmap
def write_mmap(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)
    fd = os.open(filename, os.O_RDWR)
    buf = mmap.mmap(fd, len(data))
    os.close(fd)
    return buf

# Test pickle
def write_pickle(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.
