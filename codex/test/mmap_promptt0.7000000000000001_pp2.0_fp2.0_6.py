import mmap
# Test mmap.mmap

# Open file
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Print content
    print(mm.readline())  # prints "Hello Python!"
    # Close
    mm.close()
with open('test.txt', 'r+') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())  # prints "Hello Python!"
    # Update content using file's write method.
    # Note that the content is now different
    mm.seek(0)
    mm.write(b'Hello World!')
    # Close
    mm.close()
 
# Reopen, showing changes
