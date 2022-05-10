import mmap
# Test mmap.mmap
# file = open('test.txt', 'r')

# mm = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
# print mm.readline()
# print mm.readline()
# print mm.readline()
# file.close()


# Second test
# file = open('test.txt', 'r+')
# mm = mmap.mmap(file.fileno(), 0)
# mm.write('0123456789abcdef')
# mm.seek(0)
# print mm.read(16)
# mm.close()
# file.close()

# Third test
# file = open('test.txt', 'r+')
# mm = mmap.mmap(file.fileno(), 0)
# mm.write('0123456789abcdef')
# mm.seek(0)
# print mm.read(16)
# mm.close()
# file.close()

# Fourth test
# file = open('test.txt', 'r+')
# mm = mmap.
