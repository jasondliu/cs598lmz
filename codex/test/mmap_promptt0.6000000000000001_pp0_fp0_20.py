import mmap
# Test mmap.mmap(0, length, access=mmap.ACCESS_WRITE)

length = 100
f = open('junk.txt', 'w+')
f.write('\0' * length)
f.close()

f = open('junk.txt', 'r+')
m = mmap.mmap(f.fileno(), length)
m[0:length]
m[0:length] = 'foo'
m.close()
f.close()

f = open('junk.txt', 'r')
s = f.read(length)
f.close()
assert s == 'foo'

# Test mmap.mmap(fd, 0)
# XXX Should this call fail, or map the entire file?
# XXX It currently fails.

#length = 100
#f = open('junk.txt', 'w+')
#f.write('\0' * length)
#f.close()

#f = open('junk.txt', 'r+')
#m = mmap.mmap(f.fileno(), 0)
