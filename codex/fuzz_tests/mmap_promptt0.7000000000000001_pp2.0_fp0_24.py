import mmap
# Test mmap.mmap
# Create a file
f = open('test_mmap', 'wb')
# Write 10 bytes of data to the file
f.write(b'0123456789')
f.close()
m = mmap.mmap(
    f.fileno(),
    10,
    access=mmap.ACCESS_WRITE
)

# Modify the file's content
m[0] = b'9'
m.flush()
m.seek(0)
print(m.read(10))

# Close the mmap
m.close()
