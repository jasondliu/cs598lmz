import mmap
# Test mmap.mmap()
# Test mmap.mmap(-1, size)
# Test mmap.mmap(fileno, 0)
# Test mmap.mmap(fileno, size)
# Test mmap.mmap(-1, size, flags)
# Test mmap.mmap(-1, size, flags, prot)
# Test mmap.mmap(-1, size, flags, prot, offset)
# Test mmap.mmap(-1, size, flags, prot, offset, fileno)

# Test prot values
MAP_SHARED = mmap.MAP_SHARED
#MAP_PRIVATE = mmap.MAP_PRIVATE
PROT_READ = mmap.PROT_READ
PROT_WRITE = mmap.PROT_WRITE
#PROT_EXEC = mmap.PROT_EXEC

filename = TESTFN

def check_mmap_close_after_error(m):
    try:
        f = open(filename, 'wb')
    except IOError:
        pass
    else:
        f.close()
