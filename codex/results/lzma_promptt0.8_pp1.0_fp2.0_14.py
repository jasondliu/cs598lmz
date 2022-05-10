import lzma
# Test LZMADecompressor
buf = bytearray(32)
decompressor = lzma.LZMADecompressor()
for part in b'\x80\x08\x04\x00\x10\x00\x01\x00':
    rd = decompressor.decompress(bytes([part]), buf)
    print('{!r} -> {!r}'.format(bytes([part]), buf[:rd]))

# Test LZMACompressor
compressor = lzma.LZMACompressor()
chunks = list(compressor.compress(bytes()))
print(chunks)
chunks.append(compressor.flush())
print(chunks)
