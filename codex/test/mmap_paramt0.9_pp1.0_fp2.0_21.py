import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length=1, access=mmap.ACCESS_WRITE, offset=0)
    direccion = m.find(b'\x01')
    m.close()

print(direccion)
