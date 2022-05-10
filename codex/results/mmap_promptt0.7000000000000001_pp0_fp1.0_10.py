import mmap
# Test mmap.mmap(-1, 0)
# Requires the file to be open, otherwise the fd is -1
# and mmap gets a bogus fd.
import os

# TODO:
# - test flush (also sync and sync all)
# - in-place on Windows (at least on NT)
# - test errors

#-----------------------------------------------------------------------------

def test_big():
    # Test mmap'ing a big file (1Gb)...
    # Create a 1Gb file
    f = open("big.txt", "wb")
    f.seek(1024*1024*1024)
    f.write("\0")
    f.close()
    f = open("big.txt", "r+b")
    # Open it with a mmap
    m = mmap.mmap(f.fileno(), 1024*1024*1024)
    m.close()
    f.close()
    os.remove("big.txt")

def test_close():
    f = open("junk.txt", "w+")
    f.write("1234567890")
    f.close()
   
