import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()

try:
    data = decompressor.decompress(b'\x00\x00\x00\x03\x00\x00\x00\x04')
except lzma.LZMAError as e:
    # If the compressed data doesn't end with a full block, the
    # LZMADecompressor won't be able to tell that it's at the end.
    print("Not enough data for a full block:", e)

# Finish the decompression.
decompressor.decompress(b'', True)

# There is also a way to tell the LZMADecompressor that there
# won't be any more data:
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00\x00\x00\x03\x00\x00\x00\x04',
                        unl
