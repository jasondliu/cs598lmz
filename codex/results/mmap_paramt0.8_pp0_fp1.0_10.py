import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    while True:
        print('Reading from mmap')
        if m.readline() == b'':
            print('Reading from file')
            f.write(bytes(1))
            m.flush()
