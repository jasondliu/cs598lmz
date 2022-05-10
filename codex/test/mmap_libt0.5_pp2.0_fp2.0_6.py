import mmap
import sys
import re

if len(sys.argv) < 2:
    print("Usage: python3 %s <file_to_search>" % sys.argv[0])
    sys.exit(0)

filename = sys.argv[1]

# Open the file in read-only mode
with open(filename, 'r') as f:
    # Memory-map the file, size 0 means whole file
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # Use a regular expression to find all the numbers in the file
    numbers = re.findall(b'[0-9]+', data)

print(numbers)
