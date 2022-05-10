import mmap
# Test mmap.mmap

# Open a file for writing.
# fd = os.open('/tmp/foo', os.O_RDWR | os.O_CREAT)
fd = os.open('/tmp/foo', os.O_RDWR)

# Turn on write-through mode.
# os.write(fd, b'0123456789abcdef')
# os.lseek(fd, 0, 0)

# Create a memory-map to the file.
m = mmap.mmap(fd, 16, access=mmap.ACCESS_WRITE)

# Print the original contents.
print('Before:\n{!r}'.format(m.read(16)))

# Update the memory-mapped file.
m[4:8] = b'\x00\x00\x00\x00'

# Print the updated contents.
print('After:\n{!r}'.format(m.read(16)))

# Close the memory-mapped file.
m.close()

# Close the underlying file.
os.close(fd)

#
