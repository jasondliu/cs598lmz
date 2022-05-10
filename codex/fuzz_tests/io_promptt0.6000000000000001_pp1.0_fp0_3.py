import io
# Test io.RawIOBase(<file>)

# This fails because PyFile_FromFile() returns a file object with a
# different tp_read slot than the one the file object was created with.
# The slot is changed to the slot of the file object that the file was
# opened with.

# This causes a crash because the file object's tp_read slot tries to
# use the file object's tp_read slot to move the file pointer.

f = io.FileIO('tests/io/fileio.txt', 'r')
r = io.RawIOBase(f)
r.read(1)
