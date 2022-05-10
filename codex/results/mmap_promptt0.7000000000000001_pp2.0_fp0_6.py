import mmap
# Test mmap.mmap()
#
# This test checks that mmap.mmap() can create a mmap-backed view of a file.
# It also checks that the size of a mmap-backed view can be changed.

test_size = 1024
test_file = "mmap_file"

# Create a mmap-backed view of a file
with open(test_file, "wb+") as f:
    # Create a file of size test_size
    f.seek(test_size)
    f.write(b"\0")
    f.seek(0)
    # Create a mmap-backed view of the file
    m = mmap.mmap(f.fileno(), 0)
    # Check that the size of the view is test_size
    if len(m) != test_size:
        raise RuntimeError("Incorrect size of mmap-backed view of file")
    # Change the size of the view to test_size * 2
    m.resize(test_size * 2)
    # Check that the size of the view is test_size * 2
    if len(
