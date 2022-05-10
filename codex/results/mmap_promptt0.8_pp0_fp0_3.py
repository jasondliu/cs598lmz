import mmap
# Test mmap.mmap.flush
print 'flush...',
sys.stdout.flush()
m = mmap.mmap(-1, 1)
m.write(' ')
m.flush()
m.close()
print 'OK'

# Test mmap.mmap.resize
print 'resize...',
sys.stdout.flush()
m = mmap.mmap(-1, 1)
m.resize(0)
m.close()
print 'OK'

# Test mmap.mmap.find
print 'find...',
sys.stdout.flush()
m = mmap.mmap(-1, 1)
m.write('a')
m.find('a')
m.close()
print 'OK'
