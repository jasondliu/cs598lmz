import mmap
# Test mmap.mmap
#myfile = open('/tmp/test.txt','w+')
#myfile.write('1234567890')
#myfile.close()
myfile = open('/tmp/test.txt', 'r+')
mm = mmap.mmap(myfile.fileno(), 0)
