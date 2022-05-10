import mmap
# Test mmap.mmap()
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print 'First 10 bytes via read :', m.read(10)
print 'First 10 characters via slice :', m[:10]
print '2nd   10 characters via slice :', m[10:20]
print 'Changing 1st 10 characters...',
m[:10] = '1111111111'
print '1st   10 characters via read :', m.read(10)
print 'After slice, 1st 10 characters :', m[:10]
m.close()

f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print 'First 10 bytes via read :', m.read(10)
print 'First 10 characters via slice :', m[:10]
print '2nd   10 characters via slice :', m[10:20]
print 'Changing 11th   10 characters...',
m[10:20] = '2222222222'
print '1st   10
