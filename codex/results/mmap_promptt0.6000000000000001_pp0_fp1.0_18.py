import mmap
# Test mmap.mmap(0, 1, prot=mmap.PROT_READ)
with open('/dev/zero', 'r') as f:
    m = mmap.mmap(f.fileno(), 1, prot=mmap.PROT_READ)
    print(m.read(1))
    m.close()

# Test mmap.mmap(-1, 1, prot=mmap.PROT_READ)
with open('/dev/zero', 'r') as f:
    m = mmap.mmap(-1, 1, prot=mmap.PROT_READ)
    print(m.read(1))
    m.close()

# Test mmap.mmap(0, 1, prot=mmap.PROT_WRITE)
with open('/dev/zero', 'r') as f:
    try:
        m = mmap.mmap(f.fileno(), 1, prot=mmap.PROT_WRITE)
    except ValueError as e:
        print(str(e))
    else:
        print('ValueError not raised')


