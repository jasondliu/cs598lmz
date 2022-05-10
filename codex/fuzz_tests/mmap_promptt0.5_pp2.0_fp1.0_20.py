import mmap
# Test mmap.mmap(fd, length, access=ACCESS_READ)


def check_read(name):
    f = open(name, 'rb+')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    m.close()
    f.close()


def check_write(name):
    f = open(name, 'rb+')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.close()
    f.close()


def check_read_write(name):
    f = open(name, 'rb+')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.close()
    f.close()


def check_copy(name):
    f = open(name, 'rb+')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
    m.close()
    f
