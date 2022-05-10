import mmap
# Test mmap.mmap(addr, length[, access[, flags]])

address = 0x10000
size = 0x1000

mf = mmap.mmap(-1, length=size, tagname="mmap_test")

with open("/proc/self/maps", "rt") as f:
    for line in f:
        if mf.tagname in line:
            assert(line.startswith("%x-" % address))
            break
    else:
        print("mmap test failed")
