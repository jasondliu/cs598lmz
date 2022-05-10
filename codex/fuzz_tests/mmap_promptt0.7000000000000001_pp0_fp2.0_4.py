import mmap
# Test mmap.mmap()

# Mmap from file
f = open('lorem.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
toPrint = m.readline()
print toPrint
m.close()


# Mmap from size
m = mmap.mmap(-1, 1024)
m.write('foo bar baz')
m.seek(0)
toPrint = m.readline()
print toPrint
m.close()
