import mmap
# Test mmap.mmap'ing the whole file and then trying to read past the current size


# Get the size of the file
# Stat has several values, the seventh is what we want
try:
    stat_info = os.stat(f.name)
except Exception:
    print('Failed to stat file: ' + f.name)

f.seek(0, os.SEEK_END)
print(f'Length of file: {f.tell()}')

# Set the file size to 0 for this test
f.truncate(0)
print(f'Length of file after truncation: {f.tell()}')

f.seek(0, os.SEEK_END)
print(f'Length of file after seek to end: {f.tell()}')

# Create an mmap to the file
# Try mmaping to the current length of the file
# This fails...
#mm = mmap.mmap(f.fileno(), f.tell())

# Map to the length of the file before truncation
mm = mmap.mmap(f.fileno(), stat_info
