import mmap
# Test mmap.mmap
# f = open('file.dat', 'r+b')
# m = mmap.mmap(f.fileno(), 0)
# m.write('hello world')
# m[6:] = 'mmap'
# m.seek(0)
# print repr(m.read(11))
# m.close()

# f = open('file.dat', 'r+b')
# m = mmap.mmap(f.fileno(), 0)
# m.close()

# class MMap(mmap.mmap):
#     def __init__(self, *args, **kwargs):
#         super(MMap, self).__init__(*args, **kwargs)
#         self.count = 0

#     def read(self, size):
#         self.count += 1
#         return super(MMap, self).read(size)

# f = open('file.dat', 'r+b')
# m = mmap.mmap(f.fileno(), 0)
# print m.read(10)
# print m.
