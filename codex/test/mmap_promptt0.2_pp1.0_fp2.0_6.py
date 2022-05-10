import mmap
# Test mmap.mmap()

# Create a file and write a few lines to it
with open('test.txt', 'w') as f:
    f.write('Hello world!\n')
    f.write('Bye bye world!\n')

# Open the file for reading
with open('test.txt', 'r') as f:
    # Memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Read content via standard file methods
    print(m.readline())  # prints "Hello world!"
    print(m.readline())  # prints "Bye bye world!"
    # Read content via slice notation
    print(m[:5])  # prints "Hello"
    # Close the map
    m.close()

# Open the file for writing
