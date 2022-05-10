import lzma
# Test LZMADecompressor.decompress()

# Test decompression algorithm and defaults
dec = lzma.LZMADecompressor()
indata = b'1234567890' * 1000000
infile = io.BytesIO(indata)
outdata = dec.decompress(indata)
outfile = io.BytesIO()
chunk_size = 1024
while True:
    chunk = infile.read(chunk_size)
    if len(chunk) == 0:
        break
    outfile.write(dec.decompress(chunk))
outfile.seek(0, 0)
assert outfile.read() == outdata

# Test multiple-call decompression
dec = lzma.LZMADecompressor()
assert dec.decompress(b'foo') == b'foo'
assert dec.decompress(b'bar') == b'bar'

# Test multiple-call decompression with EOF
dec = lzma.LZMADecompressor()
assert dec.decompress(b'foo', lzma.DECOMPRESS
