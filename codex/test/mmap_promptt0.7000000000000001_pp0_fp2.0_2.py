import mmap
# Test mmap.mmap()

#
# Open the file
#

f = open("/tmp/foo.txt", "r+b")
#
# Create the map
#
m = mmap.mmap(f.fileno(), 0)
#
# Print out the line that should be there
