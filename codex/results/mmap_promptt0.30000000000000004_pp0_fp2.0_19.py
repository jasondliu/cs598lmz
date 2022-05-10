import mmap
# Test mmap.mmap()
#
# This test is intended to test the mmap.mmap() function.
#
# The test will:
# - Create a file with a known size and contents.
# - mmap() the file.
# - Check the size of the mmap object.
# - Check the contents of the mmap object.
# - Write to the mmap object.
# - Check the contents of the mmap object.
# - Check the contents of the file.
# - Unmap the file.
# - Check the contents of the file.
#
# The test will fail if:
# - The size of the mmap object is not the same as the size of the file.
# - The contents of the mmap object are not the same as the file.
# - The contents of the file are not the same as the mmap object after
#   writing to the mmap object.
# - The contents of the file are not the same as the mmap object after
#   unmapping the file.
#
# This test is intended to be run manually.

# Create a file with a known size and contents.
f
