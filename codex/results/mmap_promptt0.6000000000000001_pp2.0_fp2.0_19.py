import mmap
# Test mmap.mmap()

# Run this code with:
# $ python -i mmap.py
# then run "test()" from the command prompt

def test():
    # Test mmap module
    # Based on:
    #   http://docs.python.org/library/mmap.html#mmap.mmap
    #   https://docs.python.org/2/library/mmap.html#module-mmap

    # Open a file
    f = open('test.txt', 'r+')

    # Get its size
    f.seek(0, os.SEEK_END)
    size = f.tell()

    # Memory map the file
    map = mmap.mmap(f.fileno(), size)

    # Print the file's content via the memory map
    print(map.readline())

    # Close the file
    f.close()
