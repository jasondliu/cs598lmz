from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# The LZMADecompressor class also supports an incremental interface for
# decompression. This can be used to decompress data in chunks, or to read a
# file-like object that contains a header, followed by compressed data.

with open("test.xz", "rb") as input:
    decompressor = LZMADecompressor()
    with open("test.out", "wb") as output:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            output.write(decompressor.decompress(chunk))
        output.write(decompressor.flush())

# The LZMADecompressor class also supports a 'filters' parameter which
# allows the user to specify a custom filter chain.

# The filter ID is a byte value as defined in the .xz file format
# specification. It can be given as an integer or as a bytes object.

# The filter properties is a list of integers. Each item of the list is
# an integer in little-endian format.
