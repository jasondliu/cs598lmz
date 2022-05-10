import mmap
# Test mmap.mmap(0, size, "MAP_FIXED", mmap.PROT_WRITE, fd, offset)


# Check that the second mmap can't write 0x00.
# This could use mmap.PROT_READ, but if the kernel isn't careful,
# it might copy the MMIO data into actual RAM.
with mmap.mmap(fd, 4096, mmap.MAP_FIXED, mmap.PROT_WRITE, 0) as page:
    page[:256*1024] = b'\xFF'
    page[:256*1024]
with open("/dev/urandom", "rb") as urandom:
    page[:256*1024] = urandom.read(256*1024)

try:
    page[0:256*1024:1024] = b'\x00'
    raise AssertionError("Oops - we seem to have written at an I/O address!")
except ValueError:
    pass
