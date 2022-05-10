import mmap
# Test mmap.mmap
f = open(sys.argv[1], "r+")
s = mmap.mmap(f.fileno(), 0)
pos = s.tell()

print("init pos:", pos)

s.seek(0)
print("seek(0):", s.tell())

s.seek(pos)
print("seek(pos):", s.tell())

s.seek(0, 1)
print("seek(0, 1):", s.tell())

s.seek(10, 1)
print("seek(10, 1):", s.tell())

s.seek(0, 2)
print("seek(0, 2):", s.tell())

s.seek(10, 2)
print("seek(10, 2):", s.tell())

s.seek(0)
print("seek(0):", s.tell())

s.seek(0, 0)
print("seek(0, 0):", s.tell())
