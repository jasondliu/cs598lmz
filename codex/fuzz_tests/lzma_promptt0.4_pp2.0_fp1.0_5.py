import lzma
# Test LZMADecompressor.decompress() with an empty bytestring.
# This used to raise a TypeError.
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'')
# Test LZMADecompressor.decompress() with a bytestring that is
# too short to contain a valid LZMA stream.
decompressor = lzma.LZMADecompressor()
try:
    decompressor.decompress(b'\x00')
except lzma.LZMAError as e:
    if str(e) != 'Not enough source bytes for next header':
        raise
# Test LZMADecompressor.decompress() with a bytestring that is
# too short to contain a valid LZMA stream, when the LZMA stream
# is preceded by a valid LZMA stream.
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00' * lzma.STREAM_HEADER_SIZE)
try:

