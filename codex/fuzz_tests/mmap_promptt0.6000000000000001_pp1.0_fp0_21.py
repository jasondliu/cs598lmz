import mmap
# Test mmap.mmap.tell() (issue #4010)
f = open(TESTFN, "wb+")
f.write(b"abcd")
f.flush()
m = mmap.mmap(f.fileno(), 4)
m.seek(2)
m.write(b"ef")
m.seek(0)
m.write(b"gh")
m.seek(0)
m.read(4)
m.tell()
m.seek(0, 2)
m.tell()
m.close()
f.close()
# Test mmap.mmap.seek() (issue #4010)
f = open(TESTFN, "wb+")
f.write(b"abcd")
f.flush()
m = mmap.mmap(f.fileno(), 4)
m.seek(2)
m.write(b"ef")
m.seek(0)
m.write(b"gh")
m.seek(0)
m.read(4)
m.tell()
m.seek(0, 2)
m.tell()

