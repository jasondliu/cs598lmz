import mmap
# Test mmap.mmap.read_byte
m = mmap.mmap(-1, 1)
m.write('a')

if m.read_byte() == 97:
    print "success"
else:
    print "failure"

m.close()
