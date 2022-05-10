import mmap
# Test mmap.mmap
fp = open("mmap_test.txt", "w")
fp.write("This is just a test string.")
fp.close()

fp = open("mmap_test.txt", "r+")
buf = mmap.mmap(fp.fileno(), 0) # File must be opened read-write
line = buf.readline()
print(line)
# Close file object, unlock buffer
fp.close()

# Writes to write-protected buffer do not appear on file
try:
    #buf[:15] = "ABCDEFG" # Raises TypeError exception
    pass
except TypeError as e:
    print("Raise TypeError Exception")
    print(str(e))

# Test mmap.ACCESS_READ
fp = open("mmap_test.txt", "r+")
buf = mmap.mmap(fp.fileno(), 0, mmap.ACCESS_READ)
fp.write("Write test string") # throws IOError exception
fp.close()
# Test mmap.ACCESS_COPY
