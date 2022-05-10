import lzma
# Test LZMADecompressor.seek() and LZMADecompressor.tell()

data = lzma.compress(b"hello world")

decompressor = lzma.LZMADecompressor()
decompressor.decompress(data[:2])
assert decompressor.tell() == 2
decompressor.seek(0)
assert decompressor.tell() == 0

# Test invalid seek
try:
    decompressor.seek(10)
except ValueError:
    pass
else:
    raise Exception("Expected ValueError")

# Test seek past the end
decompressor.seek(len(data))
assert decompressor.tell() == len(data)

# Test seek past the end with a non-zero offset
decompressor.seek(len(data) + 1, 1)
assert decompressor.tell() == len(data) + 1

# Test invalid seek with whence=1
try:
    decompressor.seek(-1, 1)
except ValueError:
    pass
else:
    raise Exception("Expected ValueError")

# Test invalid seek with whence
