import mmap
# Test mmap.mmap

# Create a file
f = open("test.txt", "w+")
f.write("Hello world!")
f.close()

# Open the file with mmap
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)

# Print the file
print(m.readline())

# Close the file
m.close()
f.close()

# Open the file with mmap
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)

# Replace the first word
m.seek(0)
m.write("Jello")

# Print the file
print(m.readline())

# Close the file
m.close()
f.close()

# Open the file with mmap
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)

# Replace the first word
m.seek(0)
m.write("Jello")

# Print
