import mmap
# Test mmap.mmap length accuracy

m = mmap.mmap(-1, 10)
print "Initialized 10 byte mmap object"
m.write("123456789")
print "Wrote 9 bytes to mmap object"
print "Length of mmap should now be 9, is {0}".format(len(m))
m.resize(15)
print "Resized mmap object to 15 bytes"
print "Length of mmap should now be 15, is {0}".format(len(m))
m.resize(3)
print "Resized mmap object to 3 bytes"
print "Length of mmap should now be 3, is {0}".format(len(m))
m.close()
print "Closed mmap object"
