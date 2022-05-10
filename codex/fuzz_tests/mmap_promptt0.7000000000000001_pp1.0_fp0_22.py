import mmap
# Test mmap.mmap()

# Create an empty file named "test.txt"
with open("test.txt", "wb") as f:
    pass

# Open the file as mmap
m = mmap.mmap(f.fileno(), 0)

# Write bytes to the mmap
m.write(b"Hello world!")

# Close the mmap
m.close()

# Reopen the file
with open("test.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)

    # Read the bytes from the mmap
    print(mm.readline())

    # Close the mmap
    mm.close()

# Delete the file "test.txt"
os.remove("test.txt")

# Create an empty file named "test.txt"
with open("test.txt", "wb") as f:
    pass

# Open the file as mmap
m = mmap.mmap(f.fileno(), 0)

# Write bytes to the mmap
m.write(b"Hello world!")
