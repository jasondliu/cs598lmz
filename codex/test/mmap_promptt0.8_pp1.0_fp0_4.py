import mmap
# Test mmap.mmap.
f = open('test.mmap', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Fill the contents with ASCII upper case.
m.resize(128*1024*1024)
m.write('ABCDEFGHIJKLMNOP' * (128*1024*1024/16))
