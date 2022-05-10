import mmap
# Test mmap.mmap

def test_mmap_mmap():
    # Create a file with some data.
    with open('somemap', 'wb') as f:
        f.write(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # Open the file and create an mmap.
    with open('somemap', 'r+b') as f:
        m = mmap.mmap(f.fileno(), 0)
        assert m[:] == b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # Modify the file's contents.
        m[:] = b'abcdefghijklmnopqrstuvwxyz'

        # Print the file's contents.
        print(m[:])

        # Close the mmap.
        m.close()

    # Clean up.
    os.remove('somemap')

