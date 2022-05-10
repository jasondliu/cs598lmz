import mmap
# Test mmap.mmap()
f = open(os.path.join(os.getcwd(), 'test.txt'), 'r+')
m = mmap.mmap(f.fileno(), 0)
m.write('0123456789abcdef')
m.seek(0)
