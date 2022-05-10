import mmap
# Test mmap.mmap capabilities
m = mmap.mmap(-1, 512)
m[0:8] = 'abcefgh'
# Get an empty space
m[256:] = '\0' * 256
# This will always succeed, 
# even if the file does not exist
file = open('/tmp/test.txt', 'r+b')
mf = mmap.mmap(file.fileno(), 1024)
mf[0:8] = m[0:8]
