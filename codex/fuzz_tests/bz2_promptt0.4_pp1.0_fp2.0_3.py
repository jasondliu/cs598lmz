import bz2
# Test BZ2Decompressor and BZ2Compressor
d = bz2.BZ2Decompressor()
c = bz2.BZ2Compressor()

# Test that BZ2Decompressor.unused_data is empty before any data is fed to
# decompressor.
assert d.unused_data == b''

# Test that BZ2Decompressor.unused_data is empty after decompressor is flushed
# with empty data.
d.decompress(b'')
assert d.unused_data == b''

# Test that BZ2Decompressor.unused_data is empty after decompressor is flushed
# with empty data and that decompressor remains in a usable state.
d.decompress(b'')
assert d.unused_data == b''
d.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')
assert d.unused_data == b''

# Test that BZ2Decompressor.unused_data is empty after decompressor is
