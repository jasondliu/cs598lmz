import mmap
# Test mmap.mmap

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content
print "Before:"
print m.readline()

# Move to beginning and write
m.seek(0)
m.write("Hello Python!\n")

# Read again
m.seek(0)
print "After:"
print m.readline()

# Close file
m.close()
f.close()

# Test mmap.mmap

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read content
print "Before:"
print m.readline()

# Move to beginning and write
m.seek(0)
m.write("Hello Python!\n")

# Read again
m.seek(0)
print "After:"
print m.readline()

# Close file
m.close()
f.close()


