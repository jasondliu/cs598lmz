import mmap
# Test mmap.mmap()
with mmap.mmap(-1, 128*1024) as m:
    print(m.size())
    m.seek(0)
    m.write(sys.version)
    m.seek(0)
    print(m.read(32))
    m.seek(60)
    m.write("hello")
    m.seek(60)
    print(m.read(32))

# Test mmap.mmap() with MAP_PRIVATE
with mmap.mmap(-1, 128*1024, mmap.MAP_PRIVATE) as m:
    print(m.size())
    m.seek(0)
    m.write(sys.version)
    m.seek(0)
    print(m.read(32))
    m.seek(60)
    m.write("hello")
    m.seek(60)
    print(m.read(32))

# Test mmap.mmap() with MAP_SHARED
with mmap.mmap(-1, 128*1024, mmap.MAP_SHARED)
