import lzma
# Test LZMADecompressor object
data = b'12345abcde' * 1024 * 1024 * 10
data = lzma.compress(data)
comp = lzma.LZMADecompressor()
# Try decompressing up to 32 KB of data at a time
for size in range(2**15, 2**17+1, 2**15):
    part = data[:size]
    data = data[size:]
