import lzma
# Test LZMADecompressor (LZMA decompression)
# ...
import lzma
data = b"1234567890" * 1000
compressor = lzma.LZMACompressor()
cmpdata = compressor.compress(data)
cmpdata += compressor.flush()
decompressor = lzma.LZMADecompressor()
output = decompressor.decompress(cmpdata)
len(output) == len(data)
# True
# Test LZMACompressor (LZMA compression) with various filters
# ...
# Test XZ-compressed files
# ...
data = b"1234567890" * 1000
with lzma.open("/tmp/foo.xz", "w") as fo:
    fo.write(data)
with lzma.open("/tmp/foo.xz", "r") as fo:
    output = fo.read()
len(output) == len(data)
# True
# Test BZ2-compressed files
# ...
data = b"1234567890" * 1000
with lzma.open("/tmp/
