import mmap
# Test mmap.mmap with a file that does not have a length that is a multiple of
# the system page size.
def test_non_multiples_of_page_size():
    # Create a 256-byte file.
    with open("data/odd-size.bin", "wb") as f:
        f.write(b"a" * 256)
    # Memory-map it.
    with open("data/odd-size.bin", "r+b") as f:
        m = mmap.mmap(f.fileno(), 0)
        # Write at the end of the data.
        m[255] = b"b"
    # Check the data.
    with open("data/odd-size.bin", "rb") as f:
        data = f.read()
        assert data == b"a" * 255 + b"b"
    os.unlink("data/odd-size.bin")


try:
    test_non_multiples_of_page_size()
except FileNotFoundError:
    print("Missing file: data/odd-size.bin, so skipping this
