import lzma
# Test LZMADecompressor.flush() with a truncated stream.

d = lzma.LZMADecompressor()

with open('lzma_corrupted.xz', 'rb') as f:
    data = f.read()

# Truncate the data.
data = data[:-10]

with open('lzma_corrupted_2.xz', 'wb') as f:
    f.write(data)

with open('lzma_corrupted_2.xz', 'rb') as f:
    decomp = d.decompress(f.read())

print(decomp.decode('latin1'))
</code>
It outputs:
<code>Note: For reading compressed files, use open() instead of LZMAFile.

Decompressing a compressed file
===============================

Although LZMAFile can be used to decompress a file, the LZMAFile class does
not provide readline() and readlines() functionality. For this reason, it is
usually better to use open() instead of LZMAFile.
</code>

