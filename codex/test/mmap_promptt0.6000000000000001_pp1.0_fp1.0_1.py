import mmap
# Test mmap.mmap.read_byte
m = mmap.mmap(0, 1, "")
m.write_byte(chr(1))
assert m.read_byte() == chr(1)
# Test mmap.mmap.read
m = mmap.mmap(0, 10, "")
m.write(chr(0) * 10)
assert m.read(10) == chr(0) * 10
# Test mmap.mmap.read_byte
m = mmap.mmap(0, 10, "")
m.write(chr(0) * 10)
assert m.read_byte() == chr(0)
# Test mmap.mmap.read_byte
