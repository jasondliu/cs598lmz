import mmap
# Test mmap.mmap.read function.
#
# read the whole file at once:
# readlines from anywhere in the file:

with open('python.jpg', 'rb', 0) as file, \
        mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    for line in s:
        print(line)
    print(s.readline())
    print(s.readline())
