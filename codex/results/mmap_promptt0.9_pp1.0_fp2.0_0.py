import mmap
# Test mmap.mmap
with open('/tmp/test.txt', 'w') as fp:
    fp.write('ab\n')
    fp.write('cd\n')

# Map this file
m = mmap.mmap(fp.fileno(), 0)

# Move read position to beginning
m.seek(0)

# Read line
m.readline()

# Read another line
m.readline()

# Close the mmap
m.close()
m = mmap.mmap(-1, mmap.PAGESIZE)
# Create a new anonymous mmap
m = mmap.mmap(-1, mmap.PAGESIZE)
# Add data to the anonymous mmap
m.write(b'Hello Python Learner!')
# Read from the start of the mmap
m.seek(0)
m.read(11)
# Get the size of the mmap
m.size()
# Close the mmap
m.close()
 
# Read only segment
m = mmap.mmap(fp.fileno(), 1, access=mmap.
