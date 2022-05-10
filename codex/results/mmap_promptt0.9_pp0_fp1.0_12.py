import mmap
# Test mmap.mmap
# f = open('sm', 'w+')
# f.write('0123456789')
# print f.read(5)
# f.close()
# f = open('sm', 'r+')
# m = mmap.mmap(f.fileno(), 0)
# print repr(m[3:8])
# m[3:8] = 'Kilroy'
# print repr(m[3:8])

# Test some simple reads/writes
# f = open('sm', 'w+')
# f.write('0123456789')
# f.close()
# f = open('sm', 'r+')
# m = mmap.mmap(f.fileno(), 0)
# buf = 'Four score and seven years ago...'
# m[4:4+len(buf)] = buf
# m.seek(0)
# print m.read(len(buf))
# f.close()

# test tells
# f = open('sm', 'w+')
# f.write('0123456789')

