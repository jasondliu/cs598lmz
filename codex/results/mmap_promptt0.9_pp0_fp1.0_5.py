import mmap
# Test mmap.mmap on a preopen setsize-ed file.
f = open('temp', 'w+b')
f.seek(100)
f.write(b'.')
f.close()
f = open('temp', 'r+b')
m = mmap.mmap(f.fileno(), 1, mmap.MAP_PRIVATE, mmap.PROT_READ)
if len(m) != 1:
    raise ValueError('len(m) != 1')
if m[0] != b'.'[0]:
    raise ValueError('m[0] != ord(".")')
f.close()
os.remove('temp')
# Test __setitem__ of mmap on a preopen setsize-ed file.
f = open('temp', 'w+b')
f.seek(100)
f.write(b'.')
f.close()
f = open('temp', 'w+b')
m = mmap.mmap(f.fileno(), 1, mmap.MAP_SHARED, mmap.PROT_WRITE)
m[0] =
