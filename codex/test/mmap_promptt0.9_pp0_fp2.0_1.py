import mmap
# Test mmap.mmap fails on read-only open() when O_CREAT is specified
# This is done so that mmap succeeds on read-only open() only if the
# file is already present
with pytest.raises(mmap.error):
    mmap.mmap(-1, 4096, access=mmap.ACCESS_READ, flags=mmap.MAP_SHARED, 
        prot=mmap.PROT_WRITE, fd=666, offset=0)
fp = open(TESTFN, "w+b")
fp.write(b"\0")
fp.flush()
f = mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_WRITE, 
    flags=mmap.MAP_SHARED, prot=mmap.PROT_READ, offset=0)
f[0] = b"1"[0]
f.flush()
