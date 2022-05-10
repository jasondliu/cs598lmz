import mmap
# Test mmap.mmap behavior.
# cmt: mmap.mmap creates a memory-mapped file object.

with open( "07_mmap_test.py", "r+" ) as f:
    m = mmap.mmap( f.fileno(), 0 )
    print m.readline() # prints "import mmap"

print m.size()
m.close()

with open("07_mmap_test.py", "r+" ) as f:
    # memory-map the file, size 0 means whole file
    m = mmap.mmap( f.fileno(), 0)

    # read content via standard file methods
    print m.readline() # prints "import mmap"

    # read content via slice notation
    print m[ :20 ] # prints "import mmap\n\nwith"

    # update content using slice notation;
    # note that new content must have same size
    m[ 6 : 6 ] = " memory-mapped"

    # ... and read again using standard file methods
    m.seek( 0 )
    print m.readline()
