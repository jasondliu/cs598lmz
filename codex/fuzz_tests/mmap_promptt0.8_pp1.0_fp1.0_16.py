import mmap
# Test mmap.mmap() by modifying a binary file.

def write_random(f, bufsize):
    num = bufsize / 8
    for i in range(num):
        f.write('%016x' % random.getrandbits(8 * 8))
    return bufsize

def write_random_mmap(f, bufsize):
    m = mmap.mmap(f.fileno(), 0)
    num = bufsize / 8
    for i in range(num):
        rand = '%016x' % random.getrandbits(8 * 8)
        m[i * 16 : i * 16 + 16] = rand
    m.close()
    return bufsize

def test(fname, mode, func, bufsize, rounds):
    f = open(fname, mode)
    size = 0
    for i in range(rounds):
        size += func(f, bufsize)
    f.close()
    return size

def check(fname):
    f = open(fname, 'rb')
    while True:
        chunk = f.read(
