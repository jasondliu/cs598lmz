import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
with open('/etc/hostname', 'rb') as input, \
     open('hostname.xz', 'wb') as output:
    compressor = lzma.LZMACompressor(lzma.FORMAT_XZ)
    output.write(compressor.compress(input.read()))
    output.write(compressor.flush())

with open('/etc/fstab', 'rb') as input, \
     open('fstab.xz', 'wb') as output:
    compressor = lzma.LZMACompressor(lzma.FORMAT_XZ)
    output.write(compressor.compress(input.read()))
    output.write(compressor.flush())

with open('hostname.xz', 'rb') as input, \
     open('hostname.out', 'wb') as output:
    output.write(lzc.decompress(input.read()))
