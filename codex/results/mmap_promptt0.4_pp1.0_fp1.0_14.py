import mmap
# Test mmap.mmap.read()

with open("/usr/share/dict/words") as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    print(m.read(10))
    print(m.read(10))
    print(m.read(10))
    print(m.read(10))

# Test mmap.mmap.readline()

with open("/usr/share/dict/words") as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    print(m.readline())
    print(m.readline())
    print(m.readline())
    print(m.readline())

# Test mmap.mmap.readlines()

with open("/usr/share/dict/words") as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    print(m.readlines())

# Test mmap.mmap
