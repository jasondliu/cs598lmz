from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Python 3.3+
LZMADecompressor().decompress(data)

# Python 3.3+
# This example includes a call to the decompressobj() method of
# the LZMADecompressor class.
with open('python.xz', 'rb') as input, open('python.tar', 'wb') as output:
    decompressor = LZMADecompressor()
    for chunk in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(chunk))
    output.write(decompressor.flush())

# Python 3.3+
# This example shows how to read data from a compressed file in
# multiple passes.
with open('python.xz', 'rb') as input:
    decompressor = LZMADecompressor()
    for chunk in iter(lambda: input.read(1024 * 1024), b''):
        data = decompressor.decompress(chunk)
        # Process data...

# Python 3.3
