import lzma
# Test LZMADecompressor().returncode for end-of-stream.
decompress = lzma.LZMADecompressor()
f = io.BytesIO(b'X' * 10)
h = lzma.LZMAFile(f, 'r', decompressor=decompressor)
buf = decompressor.decompress(f.read())
assert h.read() == b'X' * 10 + decompressor.unused_data
assert decompressor.unused_data == b''
assert decompressor.eof
assert decompressor.eof == decompressor.returncode == lzma.LZMA_STREAM_END
# The same, but a bit more complicated: readahead=1, read() only reads 1 byte.
decompress = lzma.LZMADecompressor()
f = io.BytesIO(b'X' * 10)
h = lzma.LZMAFile(f, 'r', decompressor=decompressor, readahead=1)
buf = decompressor.decompress(f.read())
assert h.read() == b'X' *
