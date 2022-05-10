import mmap
# Test mmap.mmap(fileno,length,flags)
# Make sure input file is at least 1024 bytes long.
f = open('test.txt','r')
m = mmap.mmap(f.fileno(),1024,mmap.MAP_SHARED,mmap.PROT_READ)
print m.readline()
print m.readline()
print m.readline()
print m.readline()
m.close()
f.close()
