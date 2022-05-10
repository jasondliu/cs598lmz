import mmap
# Test mmap.mmap(0, 0, "a")
assert msg("mem0: %s\n" % mmap.mmap(0, 0, "a")) == ""

# Test mmap.mmap(0, 4096, "a")
mem1 = mmap.mmap(0, 4096, "a")
assert len(mem1) == 4096
assert msg("mem1: %s\n" % mem1) == "mem1: b'\\0' * 4096\n"

# Test mmap.mmap(0, 1, "a")
mem2 = mmap.mmap(0, 1, "a")
assert msg("mem2: %s\n" % mem2) == "mem2: b'\\0'\n"

# Test unpacking a memoryview into several variables
x = memoryview(b"10")
lo, hi = x
assert lo == b"1"; assert hi == b"0"

# Test mmap.mmap.readinto
buf = bytearray(b"\0" * 4)
mem1.readinto(buf)
assert
