import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # write a null byte and flush to disk to "truncate" the file
    m.write_byte(b'\x00')
    m.flush()
    # print mapping as string
    print(m.read_byte())
    # print last character in file
    print(m[-1])
