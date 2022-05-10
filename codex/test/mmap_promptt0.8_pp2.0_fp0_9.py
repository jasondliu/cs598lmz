import mmap
# Test mmap.mmap.readline()

filename = "mmap_mmap_readline.txt"

# Open file with normal open
f = open(filename, "wb+")

# Put in some text
f.write(bytes("first line\n second line\n third line\n"))

# Close file as usual
f.close()

# Open file again and pass to mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Print the lines in the file
print("First line: %s" % m.readline())
print("Second line: %s" % m.readline())
print("Third line: %s" % m.readline())

# Clean up
m.close()

# The file has been closed and is not usable or necessary anymore
# os.remove(filename)

# Clean up
m.close()
f.close()
 

# Test mmap.mmap.read()

filename = "mmap_mmap_read.txt"

