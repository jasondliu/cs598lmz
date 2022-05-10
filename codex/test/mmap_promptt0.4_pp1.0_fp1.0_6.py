import mmap
# Test mmap.mmap

f = open('/tmp/test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.seek(5)
