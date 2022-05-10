import mmap
# Test mmap.mmap() on a file in read-only mode.
filename = 'example_file.txt'


# Open the file in read-only mode.
file = open(filename, "r")

# Create an empty list to store the lines of the file.
lines = []

# Read the file line by line.
for line in file:
    # Remove the "\n" at the end of each line.
    line = line.rstrip()

    # Add the line to the list.
    lines.append(line)

# Close the file.
file.close()

# Open the file in read-only mode.
file = open(filename, "r")

# Create a memory mapped file.
mm = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

# Create an empty list to store the lines of the file.
lines = []

# Read the memory mapped file line by line.
while True:
    # Read a line and remove the "\n" at the end.
    line = mm.readline().rstrip()

    # Stop
