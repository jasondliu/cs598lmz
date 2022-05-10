import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.write(b'qwer')
    print("m.read(4):{}".format(m.read(4)))

# m.read(4):b'qwer'

# resized to 3
with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access = mmap.ACCESS_WRITE)
