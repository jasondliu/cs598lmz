import mmap
# Test mmap.mmap.write_byte method

# The mmap.mmap.write_byte() method writes a single byte to the memory
# map, at the specified offset.

# Syntax
# Following is the syntax for write_byte() method −

# os.write_byte(offset, byte);
# Parameters
# offset − This is the offset in bytes where the byte is to be written.

# byte − This is the byte to be written.

# Return Value
# This method does not return any value.

# Example
# The following example shows the usage of write_byte() method.

import os, mmap

# Open file
fd = os.open( 'foo.txt', os.O_CREAT | os.O_RDWR )

# Create mmap object
m = mmap.mmap( fd, 0 )

# Write byte
m.write_byte( 'B' )

# Close the file
os.close( fd )
