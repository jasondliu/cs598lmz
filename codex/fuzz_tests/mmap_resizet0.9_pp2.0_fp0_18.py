import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m.read()
    c = m.read_byte()
    d = m.readline()
    e = m.readline()

class F(object):
    def readable(self):
        return True

    def read(self):
        return b'1'

mmap.mmap(F(), 1)

i = mmap.mmap(0, 1)
i.read(1)
i.readline()
i.readline()
i.tell()
i.move(0, 3)
i.seek(0, 1)
