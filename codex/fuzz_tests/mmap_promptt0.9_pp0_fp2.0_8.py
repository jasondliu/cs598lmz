import mmap
# Test mmap.mmap mem = mmap.mmap(fd, 4096, "rwx"); 
#mem.read(4) # display first four bytes mem.write(b'\x00') # write the null character '\x00'
#mem.close() # don't forget to close

# Define a function that steps through a memory map from a file descriptor
def mmapstepper(fobject, steplen = 1, newlinechar = '\n'):
    """Use mmap to step through a file, given a file object."""
    # step through a memory map of the file object
    mem = mmap.mmap(fobject.fileno(), 0, "rwx")
    while True:
        # Read the next block of steplen bytes
        out = mem.read(steplen)
        # Break the while if the read returns an empty string
        if not out:
            break
        # Use the yield function to return the next read value
        yield out
    # Close the memory map and return/exit.  This will also raise a StopIteration
    # exception.
    mem.close
