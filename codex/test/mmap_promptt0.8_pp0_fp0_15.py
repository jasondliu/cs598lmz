import mmap
# Test mmap.mmap.read()
fp = open("/usr/share/dict/words", "r")
m = mmap.mmap(fp.fileno(), 0, "r", mmap.MAP_SHARED, mmap.PROT_READ)
# Read the entire string in the map
all_bytes = m.read(m.size())
print("Read all:")
print(all_bytes)
# Test mmap.mmap.read_byte()
# Incrementally read the byte value
print("Read byte by byte:")
for i in range(m.size()):
    print("m[{}] = {}".format(i, m.read_byte()))
# Test mmap.mmap.read_line()
print("Read lines:")
pos = m.tell()
while True:
    line = m.read_line()
    if not line:
        break
    print("m[{}:{}] = {}".format(pos, m.tell(), line))
    pos = m.tell()

fp.close()
