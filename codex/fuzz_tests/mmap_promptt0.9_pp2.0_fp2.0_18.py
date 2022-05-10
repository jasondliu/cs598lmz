import mmap
# Test mmap.mmap
mem = mmap.mmap(fd, 10, access=mmap.ACCESS_WRITE)  # write-only
mem[3] = '2'
mem.close()
a = mmap.mmap(
    fd, 10,
    access=mmap.ACCESS_COPY   # copy-on-write
)  # Here, `mem` is read-only.
a.seek(0)
print(a.read(10))   # b'1234890\n'
a[3] = '3'          # RuntimeError: can't set
a.flush()           # RuntimeError: cannot writemmap object
a.close()
a = mmap.mmap(
    fd, 10,
    access=mmap.ACCESS_WRITE
)  # Write access.
a[3] = '9'
a.close()
f = open('example.bin', 'rb')
f.seek(5)
print(f.read(1))   # b'9'
f.close()

# 2.3 Using Slots to Save
