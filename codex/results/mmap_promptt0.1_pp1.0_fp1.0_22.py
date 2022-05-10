import mmap
# Test mmap.mmap()

# Open file for reading
with open("lorem.txt", "r") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read content via standard file methods
    print(mm.readline())  # prints "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\n"
    # read content as byte array
    print(mm[:5])  # prints "Lorem"
    # close the map
    mm.close()

# Open file for writing
with open("lorem2.txt", "w+") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # write to the file
    mm.write(b"Hello Python!\n")
    # read from the file
    print(mm.readline())  # prints "Hello Python!\n"
    # close the map

