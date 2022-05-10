import mmap
# Test mmap.mmap

def test_mmap():
    """
    >>> test_mmap()
    """
    # Create a memory mapped file
    fd = os.open('/dev/zero', os.O_RDWR)
    m = mmap.mmap(fd, 4096)

    # Print the size of the mapped file
    print(len(m))

    # Read the first 4 bytes
    print(m[0:4])

    # Read the last 4 bytes
    print(m[-4:])

    # Read the first 4 bytes
    print(m[0:4])

    # Read the last 4 bytes
    print(m[-4:])

    # Update the first 4 bytes
    m[0:4] = b'1234'

    # Read the first 4 bytes
    print(m[0:4])

    # Read the last 4 bytes
    print(m[-4:])

    # Update the last 4 bytes
    m[-4:] = b'5678'

    # Read the first 4 bytes
    print(m[0:4])

    #
