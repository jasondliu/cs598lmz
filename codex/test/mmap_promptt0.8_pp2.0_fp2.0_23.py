import mmap
# Test mmap.mmap()
map = mmap.mmap('/tmp/foo', 1, ok, access=mmap.ACCESS_READ)
map.flush()
map.close()
map.lock()
map.seek(0)
map.seek(0, 0)
map.find(0)
map.rfind(0)
map.tell()
map.move(0, 0, 0)
map.read(1)
map.read_byte()
map.readline(1)
map.readline()
map.readlines(1)
map.readlines()
map.write(0)
map.write_byte(0)
map.writelines(0)
map.unlock()
map.flush()
map.close()
map.seek(0)
map.seek(0, 0)
map.read(1)
map.read_byte()
map.readline(1)
map.readline()
map.readlines(1)
map.readlines()
map.tell()
map.size()
map.tell()
