import mmap
import sys

# Open a file
fd = os.open( "foo.txt", os.O_RDWR )

# Memory-map the file, size 0 means whole file
m = mmap.mmap( fd, 0 )

# Read content via standard file methods
print m.readline()  # prints "Hello Python!\n"

# Update content using slice notation;
# note that new content must have same size
m[6:] = " world!\n"

# ... and read again using standard file methods
m.seek(0)
print m.readline()  # prints "Hello  world!\n"

# close the map
m.close()

# close the file
os.close( fd )
</code>

