import mmap
# Test mmap.mmap()
#
# This test is a little unusual in that it uses a file that is already
# created.  It is the file "test.mmap", which is created by running
# the test_mmap_write.py test.  This test is also unusual in that it
# does not create a new mmap object.  It uses the mmap object created
# by the test_mmap_write.py test.
#
# This test is run by test_mmap_write.py.  It is not run by regrtest.py.

# Create a mmap object from the file "test.mmap".  The file was created
# by the test_mmap_write.py test.
f = open("test.mmap", "r+b")
m = mmap.mmap(f.fileno(), 0)

# Read the data from the mmap object.
data = m.read(100)

# Check that the data is correct.
if data != "hello world":
    raise RuntimeError, "data read from mmap object is incorrect"

# Close the mmap object
