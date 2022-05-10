import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = b'.'
while True:
    # Feed data in piece by piece, until you have
    # all of the original data
    buf = decompressor.decompress(data)
    if buf:
        print(buf)
    if decompressor.eof:
        break
    data = b'.'

# Flush the decompressor, to get any remaining data
buf = decompressor.flush()
if buf:
    print(buf)

# Decompress a file
with open('lorem.txt.xz', 'rb') as input, \
     open('lorem.txt', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    for data in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(data))
    output.write(decompressor.flush())

# Decompress
