import mmap
# Test mmap.mmap(3,length)
m = mmap.mmap(3,65536)
# Test mmap.mmap(3,length,flags)
m = mmap.mmap(3,65536,mmap.MAP_SHARED)
# Test mmap.mmap(3,length,prot,flags)
m = mmap.mmap(3,65536,mmap.PROT_READ,mmap.MAP_SHARED)
# Test mmap.mmap(3,length,prot,flags,offset)
m = mmap.mmap(3,65536,mmap.PROT_READ,mmap.MAP_SHARED,0)
# Test mmap.mmap(3,length,prot,flags,offset,fd)
m = mmap.mmap(3,65536,mmap.PROT_READ,mmap.MAP_SHARED,0,3)
# Test mmap.mmap(3,length,prot,flags,offset,fd,closefd)
m = mmap.mmap(3,65536,mmap.PR
