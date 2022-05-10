import mmap
# Test mmap.mmap(fileno, length [, access [, offset]])
m = mmap.mmap(-1, 10,mmap.MAP_SHARED, mmap.PROT_WRITE )
m.write(b"1234567890")
if m.read(5) != b"12345":
    print("ERROR#1")
if m.size() != 10:
    print("ERROR#2")

if m.seek(3) != 3:
    print("ERROR#3")

if m.tell() != 3:
    print("ERROR#4")

if m.read(5) != b"45678":
    print("ERROR#5")

if m.seek(0, mmap.SEEK_END) != 10:
    print("ERROR#6")

if m.tell() != 10:
    print("ERROR#7")

if m.read(10) != b"":
    print("ERROR#8")

if m.seek(12) != 0:
    print("ERROR#9")

m.write(b"1234")

