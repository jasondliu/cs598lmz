import mmap
# Test mmap.mmap
# No such file or directory
# Traceback (most recent call last):
#   File "C:\Users\M\Desktop\Code\Python\mmap_test.py", line 7, in <module>
#     m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# OSError: [Errno 2] No such file or directory
#
# f = open('test.txt', 'w+')
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# m.write(b'Hello Python!')
# m.close()
# f.close()
#
# f = open('test.txt', 'r+')
# m = mmap.mmap(f.fileno(), 0)
# print(m.read(1))
# print(m.readline())
# print(m.readline())
# print(m.readline())
# print(m.readline())
# print(m.readline())
# m.
