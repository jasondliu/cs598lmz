import mmap
# Test mmap.mmap

import mmap

with open("/tmp/foo.txt", "w+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b"Hello Python!\n")
    mm.seek(0)
    print(mm.readline())
    mm.close()

print("--" * 30)

with open("/tmp/foo.txt", "w+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b"Hello Python!\n")
    print(mm[:5])
    print(mm[6:])
    mm.close()

print("--" * 30)

with open("/tmp/foo.txt", "w+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write(b"0123456789abcdef")
    mm.seek(0)
    print(mm.read(1))
    mm.seek(0)
    print(mm.read
