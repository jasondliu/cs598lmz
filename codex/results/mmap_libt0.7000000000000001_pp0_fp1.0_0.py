import mmap
import sys

# Process command line arguments
file_name = sys.argv[1]

# Open the file
fd = os.open(file_name, os.O_RDWR)

# Create a new mmap
m = mmap.mmap(fd, 0)

# Print the file
print(repr(m.read(1024)))

# Close the file
os.close(fd)
</code>

<code>$ python3 mmap_write.py testdata
b'This is a test data string.\n'
</code>

