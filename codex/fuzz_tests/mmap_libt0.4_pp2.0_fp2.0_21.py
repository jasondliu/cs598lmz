import mmap
import numpy as np
import time
import sys

# Start timer
start_time = time.time()

# Get file name from command line
if len(sys.argv) < 2:
    print "Please specify a file name."
    sys.exit()

# Open file
file_name = sys.argv[1]
f = open(file_name, "r+")

# Memory map the file
mm = mmap.mmap(f.fileno(), 0)

# Find the start and end of the data
start = mm.find('[')
end = mm.rfind(']')

# Convert data to numpy array
data = np.array(eval(mm[start:end+1]))

# Find the number of rows and columns
rows, cols = data.shape

# Find the number of elements
num_elements = rows * cols

# Find the number of bytes
num_bytes = data.nbytes

# Find the number of bits
num_bits = num_bytes * 8

# Print results
print "Number of
