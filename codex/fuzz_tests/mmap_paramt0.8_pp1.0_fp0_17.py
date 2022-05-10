import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print binascii.hexlify(m)
    m.write_byte(7)
    print binascii.hexlify(m)
    m.seek(0)
    print binascii.hexlify(m)
    print m.read(1)
    m.close()
