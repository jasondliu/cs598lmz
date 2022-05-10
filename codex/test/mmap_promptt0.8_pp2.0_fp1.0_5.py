import mmap
# Test mmap.mmap
f = open("/dev/mem", "r+b")
mem = mmap.mmap(f.fileno(), 0xffff, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0)
print(mem[0:4])
mem[0:4] = b"\x01\x02\x03\x04"
