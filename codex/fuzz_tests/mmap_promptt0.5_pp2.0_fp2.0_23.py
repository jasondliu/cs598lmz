import mmap
# Test mmap.mmap for a file

def main():
    # Open a file for reading.
    f = open('lorem.txt', 'r+')
    # Create a memory-map to the file, size 0 means whole file.
    m = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods.
    print(m.readline())  # prints "Hello Python!\n"
    # Update content using file methods.
    m.seek(0)  # rewind
    m.write('Hello World!\n')
    # Update content using slice notation.
    # ... and read using standard file methods.
    m[6:] = 'Python!'
    m.seek(0)
    print(m.readline())  # prints "Hello Python!\n"
    # Close the map and file.
    m.close()
    f.close()

if __name__ == '__main__':
    main()

# If the file is small enough to fit in memory, mmap() is faster than a simple read() or write() by a factor of 10
