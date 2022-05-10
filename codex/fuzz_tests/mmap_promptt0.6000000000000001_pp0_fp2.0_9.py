import mmap
# Test mmap.mmap()
print "Test mmap.mmap()"

# Create a buffer
buf = mmap.mmap(-1, 10)
print "Created a buffer of length", len(buf)

# Write a string to the buffer
buf.write('Hello ')
print "Wrote a string to the buffer"

# Read a string from the buffer
print "Read a string from the buffer:", buf.read(6)

# Read the rest of the buffer
print "Read the rest of the buffer:", buf.read()

# Close the buffer
buf.close()
print "Closed the buffer."
