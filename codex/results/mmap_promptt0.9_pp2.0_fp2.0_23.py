import mmap
# Test mmap.mmap.__init__()
POS,SIZE = 0,10
f = os.tmpfile()
m = mmap.mmap(f.fileno(), SIZE, access=mmap.ACCESS_WRITE)
m[POS] = '\0'
m.close()
# Test mmap.mmap.move()
POS1,POS2,SIZE = 0,10,10
f = os.tmpfile()
m = mmap.mmap(f.fileno(), SIZE, access=mmap.ACCESS_WRITE)
m[POS1:POS1 + SIZE] = 'foo'
m[POS2:POS2 + SIZE] = 'bar'
m.move(POS1,POS2,SIZE)
value = m[POS2].strip('\x00')
m.close()
# Test mmap.mmap.read()
POS,SIZE = 0,10
VERIFY = '1234567890'
f = os.tmpfile()
f.write(VERIFY)
f.flush()
m = mmap.mmap(f.fileno(),
