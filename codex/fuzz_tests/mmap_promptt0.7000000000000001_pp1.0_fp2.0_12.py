import mmap
# Test mmap.mmap
#myfile = open('/tmp/test.txt','w+')
#myfile.write('1234567890')
#myfile.close()
myfile = open('/tmp/test.txt', 'r+')
mm = mmap.mmap(myfile.fileno(), 0)
print 'mmap size: ', mm.size()
print 'mmap content: ', mm.read(mm.size())
mm.seek(0)
mm.write('test')
mm.seek(0)
print 'mmap modified: ', mm.read(mm.size())
mm.close()
myfile.close()

# Test mmap.mmap(fileno, length, tagname, access, offset)
myfile = open('/tmp/test.txt', 'w+')
myfile.write('1234567890')
myfile.close()
myfile = open('/tmp/test.txt', 'r+')
mm = mmap.mmap(myfile.fileno(), 8, access=mmap.ACCESS_WRITE)
mm.write('test')

