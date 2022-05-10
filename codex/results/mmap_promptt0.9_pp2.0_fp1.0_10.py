import mmap
# Test mmap.mmap

file = mmap.mmap(3,1,access=1)

file.write(b'A')

command = mmap.mmap(12,32,access=1)

memoryBuffer = mmap.mmap(3400,1,access=1)

# mmap.mmap()	
# mmap.ACCESS_COPY	
# mmap.ACCESS_READ	
# mmap.ACCESS_WRITE	
# mmap.ALLOCATIONGRANULARITY	
# mmap.MAP_ANON	
# mmap.MAP_ANONYMOUS	
# mmap.MAP_DENYWRITE	
# mmap.MAP_EXECUTABLE	
# mmap.MAP_FIXED	
# mmap.MAP_GROWSDOWN	
# mmap.MAP_HASSEMAPHORE	
# mmap.MAP_NORESERVE	
# mmap.MAP_POPULATE	
# mmap.MAP_SHARED	
# mmap.MAP_SHARED_VALIDATE	
#
