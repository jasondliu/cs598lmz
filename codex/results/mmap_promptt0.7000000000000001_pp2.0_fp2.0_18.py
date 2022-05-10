import mmap
# Test mmap.mmap().write_byte()

with open("tmp", "wb+") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'A')
    m.seek(0)
    print(m.read_byte())
    m.close()

with open("tmp", "rb") as f:
    b = f.read()
    print(b)

os.remove("tmp")
