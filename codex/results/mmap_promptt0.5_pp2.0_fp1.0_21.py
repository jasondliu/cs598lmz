import mmap
# Test mmap.mmap

# Open a file
f = open("test.txt", "w+")

# Write a string to the file
f.write("Hello, world!")

# Close the file
f.close()

# Open the file
f = open("test.txt", "r+")

# Map the file into memory
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
print(m[:])

# Close the file
f.close()

# Open the file
f = open("test.txt", "w+")

# Write a string to the file
f.write("Hello, world!")

# Close the file
f.close()

# Open the file
f = open("test.txt", "r+")

# Map the file into memory
m = mmap.mmap(f.fileno(), 0)

# Print the first character
print(m[0])

# Print the entire file
print(m[:])

# Print the last character
print(m[-1])

#
