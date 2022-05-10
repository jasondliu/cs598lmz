import mmap
# Test mmap.mmap()
# Open file
f = open('data.dat','r+b')
# Create mmap
m = mmap.mmap(f.fileno(),0)
# Read value at address 0
m.seek(0)
s = m.read(8)
print('Read:',s)
# Write value at address 0
m.seek(0)
m.write(b'01234567')
m.flush()
m.seek(0)
s = m.read(8)
print('Read:',s)
# Close mmap
m.close()
# Close file
f.close()

# Test mmap.mmap() with offset
# Open file
f = open('data.dat','r+b')
# Create mmap
m = mmap.mmap(f.fileno(),80,access=mmap.ACCESS_WRITE,offset=16)
# Read value at address 0
m.seek(0)
s = m.read(8)
print('Read:',s)
# Write value at address 0
m.seek(0)

