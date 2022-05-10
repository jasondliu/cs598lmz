import mmap
# Test mmap.mmap
# mm = mmap.mmap(fileno, length, access, flag)
with open("aValidFile", "w+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    f.write(b"\0")
    assert mm[:] == b"\0"
    assert mm.read(1) == b"\0"
    mm.write(b"a")
    assert mm[:] == b"a"
    assert mm.read(1) == b"a"
    mm.close()


import cmath
# Test cmath.rect
assert cmath.rect(1.0, 2.0) == complex(1.0, 2.0)

# Test complex relative to __cmp__
assert complex(1, 1) == complex(1, 1)
assert complex(1, 1) == 1+1j
assert complex(1, 1) != 1-1j
assert not (complex(1, 1) == "not a complex")
assert complex(1, 1) != "not a complex"
