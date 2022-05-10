import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 1024, "OSM_Provider", mmap.ACCESS_WRITE)

m[0:].encode("utf-8")
m.write(b"\x00\x01")

m.read(1)
m.read(1)

m.close()

# Test mmap.mmap(-1, ...)
m = mmap.mmap(-1, 1024, "OSM_Provider", mmap.ACCESS_WRITE)

m[0:].encode("utf-8")
m.write(b"\x00\x01")

m.read(1)
m.read(1)

m.close()

# Test mmap.mmap(0, 0, ...)
m = mmap.mmap(0, 0, "OSM_Provider", mmap.ACCESS_WRITE)

m[0:].encode("utf-8")
m.write(b"\x00\x01")

m.read(1)
