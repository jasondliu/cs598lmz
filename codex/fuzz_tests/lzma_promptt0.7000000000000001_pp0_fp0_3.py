import lzma
# Test LZMADecompressor.read()

decompressor = lzma.LZMADecompressor()

# Feed the decompressor with bytes until it needs more input
# and the EOF flag is set.
data = b''
with open('data.lzma', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if len(chunk) == 0:
            break
        data += decompressor.decompress(chunk)

print(data, end='')

# Decompressor.eof flag is set after the last byte
# was read from the compressed stream.
assert decompressor.eof
# Test LZMADecompressor.decompress()

decompressor = lzma.LZMADecompressor()

# Decompress the whole file at once.
with open('data.lzma', 'rb') as f:
    data = decompressor.decompress(f.read())

print(data, end='')

# Decompressor.eof flag is set after the last byte
# was
