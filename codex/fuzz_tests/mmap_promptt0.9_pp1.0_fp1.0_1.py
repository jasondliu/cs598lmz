import mmap
# Test mmap.mmap() doesn't segfault, and
# ensures that modifying the mmapped region
# affects the file.
# In particular, test that mmap.mmap + numpy.frombuffer(..)
# doesn't segfault.

fn = "/tmp/tmp_file.dat"
foo = mmap.mmap(0, 0x1000, fn, mmap.ACCESS_WRITE)
foo.resize(0x100)
bar = array.array('i', range(0x100)).tostring()
foo[:] = bar
foo.close()

f = open(fn,'r+')
foo = mmap.mmap(f.fileno(), 0x1000)
assert len(foo) == 0x100
assert foo[:] == bar
foo.close()
f.close()

foo = mmap.mmap(-1, 0x1000, fn, mmap.ACCESS_WRITE)
foo.resize(0x100)
bar = array.array('i', range(0,0x100,2)).tostring()
foo[:] = bar
