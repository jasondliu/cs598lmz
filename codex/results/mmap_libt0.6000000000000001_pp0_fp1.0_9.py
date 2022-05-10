import mmap
import random
import time
import sys
import os

# Set the filename and open the file
filename = sys.argv[1]
f = open(filename, 'r+')

# Memory-map the file, size 0 means whole file
map = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
#print 'First ten characters are:', map[:10]

# Read content via slice notation
#print 'First ten characters are:', map[0:10]

# Update content using slice notation;
# note that new content must have same size
#map[0:10] = '0123456789'

# ... and read again using standard file methods
#print 'First ten characters are:', map[:10]

# Close the map
#map.close()

#print 'First ten characters are:', map[:10]

#map = mmap.mmap(f.fileno(), 0)

#map.seek(0)

#print 'First ten characters are:', map[:10]


