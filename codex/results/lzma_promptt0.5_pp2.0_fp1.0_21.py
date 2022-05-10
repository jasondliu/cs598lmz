import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()

with open("test.xz", "rb") as f:
    data = f.read()

decompressed = decompressor.decompress(data)

print(decompressed)

# Test LZMAFile.
with lzma.open("test.xz", "rb") as f:
    data = f.read()

print(data)
</code>
Output:
<code>b'This is some test data.'
b'This is some test data.'
</code>

