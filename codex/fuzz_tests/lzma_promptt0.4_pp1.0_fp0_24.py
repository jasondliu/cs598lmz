import lzma
# Test LZMADecompressor.

# This test is not run automatically. Run it manually.

# Create a file with a lot of random data.
f = open("test.lzma", "wb")
f.write(lzma.LZMACompressor().compress(b"".join(
    bytes([random.randint(0, 255)]) for i in range(1000000))))
f.close()

# Decompress it.
f = open("test.lzma", "rb")
d = lzma.LZMADecompressor()
data = f.read(1)
while data:
    data = d.decompress(data)
    if data:
        print(len(data))
    data = f.read(1)
f.close()
