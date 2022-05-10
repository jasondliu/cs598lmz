import mmap
# Test mmap.mmap()

# Open file
fd = os.open('/tmp/mmaptest', os.O_RDWR | os.O_CREAT)

# Zero out the file to lengthen it
assert os.write(fd, '\x00' * 1024) == 1024

# Create the mmap instace with the following params:
# fd: File descriptor which will be used for the mmapping.
# length: Must be a multiple of the page size as returned by os.sysconf('SC_PAGE_SIZE')
# flags: MAP_SHARED means other processes can share this mmap
# prot: PROT_WRITE means this process can write to this mmap
buf = mmap.mmap(fd, 1024, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Close the fd, which will cause the mmap to remain
os.close(fd)

# Print out the buffer's entire contents
print buf[:]

# Print out the first 5 bytes of the buffer
print buf[:5]

# Update the first 5 bytes
buf[:5
