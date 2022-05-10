import mmap
# Test mmap.mmap.close(), which is not called in the destructor when
# MAP_SHARED is specified.  We need the map to be big enough that the
# underlying file will not be mapped into memory.  Use /dev/null as the
# file to map.
with open('/dev/null', 'rb') as f:
    m = mmap.mmap(f.fileno(), 8192, access=mmap.ACCESS_READ)
    m.close()
    try:
        m.wri
