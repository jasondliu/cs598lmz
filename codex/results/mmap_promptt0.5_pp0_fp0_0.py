import mmap
# Test mmap.mmap()
#
# NOTE: This test is not complete and is not run by pytest.
#       It is just a scratchpad for me to try out things.

# https://docs.python.org/3/library/mmap.html

# Access modes:
# r: read-only
# w: write-only (initializes the file with zeros)
# a: write-only (appends to the end of the file)
# r+: read-write
# w+: write-read (initializes the file with zeros)
# a+: write-read (appends to the end of the file)

# Open a file for writing.
# f = open("data.bin", "wb")
# f.write(b"Hello Python!\n")
# f.close()

# Open the file for reading.
# f = open("data.bin", "r+b")

# Memory-map the file, size 0 means whole file.
# m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods.
# print
