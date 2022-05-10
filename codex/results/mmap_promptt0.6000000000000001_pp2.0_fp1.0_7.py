import mmap
# Test mmap.mmap()

# Create a file and write a line of text to it
f = open('myfile', 'w')
f.write('hello world\n')
f.close()

# Open the file for reading
f = open('myfile', 'r')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read the content via standard file methods
print m.readline()

# Close the map
m.close()

# Close the file
f.close()

# Open the file for reading
f = open('myfile', 'r')

# Create a mmap object, asking for the whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the length of the file, using the standard file method
print len(m)

# Close the map
m.close()

# Close the file
f.close()

# Open the file for writing
f = open('myfile', 'r+')
