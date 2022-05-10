import mmap
# Test mmap.mmap.readline()

# Read a file containing "Hello"
with open("test_mmap_readline.txt", "w+") as f:
    f.write("Hello")

# Map the file
with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
    # Read the first line
    line = m.readline()
    print("First line:", line)

# Read the rest of the file
line = m.readline()
print("Next line:", line)

# There is no more data, so readline() returns an empty string
line = m.readline()
print("Next line:", line)

# Test mmap.mmap.find()

# Read a file containing "Hello"
with open("test_mmap_find.txt", "w+") as f:
    f.write("Hello")

# Map the file
