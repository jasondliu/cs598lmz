import lzma
# Test LZMADecompressor.eof()

# Create a decompressor and feed it some data
d = lzma.LZMADecompressor()
result = d.decompress(b'\x00\x00\x00\x00')

if d.eof:
    print('EOF reached')
else:
    print('EOF not reached')

# Feed the decompressor some more data
result += d.decompress(b'\x00\x00\x00\x00')

if d.eof:
    print('EOF reached')
else:
    print('EOF not reached')

# Feed the decompressor all remaining data
result += d.decompress(b'\x00\x00\x00\x00')

if d.eof:
    print('EOF reached')
else:
    print('EOF not reached')

# Try to decompress more data
try:
    result += d.decompress(b'\x00\x00\x00\x00')
except EOFError:
    print('EOF
