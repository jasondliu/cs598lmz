import mmap
# Test mmap.mmap and mmap.ACCESS_COPY
m = mmap.mmap(1,16)
m.write(b"abcdefghijklmnop")
assert m[:5] == b"abcde"
assert m[5:11] == b"fghijk"
del m

m = mmap.mmap(1,16,flags=mmap.MAP_PRIVATE,prot=mmap.PROT_READ)
assert m[:5] == b"abcde"
try:
    m[0] = b"!"
except ValueError:
    pass
else:
    raise RuntimeError("mmap.PROT_READ did not prevent write")

del m

# Test mmap.mmap.find
m = mmap.mmap(1,16)
m.write(b"abcdefghijklemno")
assert m.find(b"kl") == 10
assert m.find(b"zz") == -1

m[5:9] = b"zzzz"
assert m.find(b"zz") == 5

