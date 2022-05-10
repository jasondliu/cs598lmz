import mmap
# Test mmap.mmap.read_byte()

with open("tmp.txt", "w+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.write("ABCDEFGHI")
    print(mm.read_byte())
    print(mm.read_byte())
    print(mm.read_byte())
    mm.close()

with open("tmp.txt", "r+") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.readline())
    mm.close()

# $ python3 mmap_read_byte.py
# 65
# 66
# 67
# b'ABCDEFGHI'
