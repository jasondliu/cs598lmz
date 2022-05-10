import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # run this 10 times and you'll see nothing in the file
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1
