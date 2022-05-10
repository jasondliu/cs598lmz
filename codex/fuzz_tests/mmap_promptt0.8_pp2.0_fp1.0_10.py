import mmap
# Test mmap.mmap
# Python cookbook: 
# http://code.activestate.com/recipes/52215/

# http://stackoverflow.com/questions/2927139/c-how-to-read-text-from-binary-file-into-a-char-array    

# Get read-only access to the whole file
print "Creating mmap"
f = open('test.txt', 'r+')
filename = mmap.mmap(f.fileno(), 0)

# Start at the beginning
filename.seek(0)

# Read the first line
print "First line:"
print filename.readline()

# Go back, then skip the first line
print "Second line:"
filename.seek(0)
filename.readline()
print filename.readline()

# Go back to the beginning
print "First line again:"
filename.seek(0)
print filename.readline()

# Close the file
print "Closing mmap"
filename.close()

#print "Closing file"
f.close()
