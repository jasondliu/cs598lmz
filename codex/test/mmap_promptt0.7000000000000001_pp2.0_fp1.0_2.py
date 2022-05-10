import mmap
# Test mmap.mmap
# f = open('/tmp/test.txt', 'wb+')
# mm = mmap.mmap(f.fileno(), 0)
# mm.write('Hello')
# mm.seek(0)
# print(mm.readline())
# mm.close()
# f.close()

# Test mmap.mmap with a string
# s = mmap.mmap(-1, 1024)
# s.write('Hello')
# print(s.find('H'))
# print(s.readline())

# Test mmap.mmap with a file-like object
# f = open('/tmp/test.txt', 'w+b')
# m = mmap.mmap(f.fileno(), 0)
# m.write('Hello World')
# m.seek(0)
# while True:
#     c = m.read(1)
#     if not c:
#         break
#     print(c)
# m.close()

# Test mmap.mmap with anonymous memory
# m = mmap.mmap(-1
