import mmap
# Test mmap.mmap(fd, length, flags, prot, access, offset)
m = mmap.mmap(-1, 4096)
m[0:10] = "0123456789"
print m[0:10]
m.close()

# Test mmap.mmap(fileno, length, flags, prot, access, offset)
m = mmap.mmap(sys.stdout.fileno(), 4096)
m[0:10] = "0123456789"
print m[0:10]
m.close()

# Test mmap.mmap(fd, length, flags, prot, access, offset)
m = mmap.mmap(sys.stdout, 4096)
m[0:10] = "0123456789"
print m[0:10]
m.close()

# Test mmap.mmap(fd, length, flags, prot, access, offset)
m = mmap.mmap(sys.stdout, 4096, prot=mmap.PROT_WRITE)
m[0:10] = "0123456789"

