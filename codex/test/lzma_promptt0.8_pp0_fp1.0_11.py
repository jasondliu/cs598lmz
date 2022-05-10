import lzma
# Test LZMADecompressor

def print_decompressed(d, bufsize=1024):
    """
        Prints out decompressed data from the LZMA Decompressor object d,
        without printing the trailing EOF.
    """
    if hasattr(d, "unused_data"):
        # Python 3.5+
        unused_data = d.unused_data
        while True:
            try:
                data = d.decompress(bufsize)
            except EOFError:
                break
        print(data, end="")
        unused_data = d.unused_data
    else:
        while True:
            try:
                data = d.decompress(bufsize)
            except EOFError:
                break
            print(data, end="")

