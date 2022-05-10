import mmap
# Test mmap.mmap.move
with open("test_file", "wb") as f:
    f.seek(11412)
    f.write(b'\x00')
    f.flush()
f.close()

with open("test_file", "r+b") as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print(m[:10])
        m.move(100, 0, 10)
        print(m[:10])
        m.move(0, 100, 10)
        print(m[:10])
        m.close()
