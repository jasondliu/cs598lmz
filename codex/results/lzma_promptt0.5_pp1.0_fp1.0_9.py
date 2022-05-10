import lzma
# Test LZMADecompressor.

c = lzma.LZMACompressor()

# Create a test file.
with open('test.lzma', 'wb') as f:
    f.write(c.compress(b"Hello world!\n"))
    f.write(c.compress(b"Goodbye world!\n"))
    f.write(c.flush())

# Read the compressed file.
with open('test.lzma', 'rb') as f:
    d = lzma.LZMADecompressor()
    for chunk in iter(lambda: f.read(32 * 1024), b''):
        print(d.decompress(chunk))
