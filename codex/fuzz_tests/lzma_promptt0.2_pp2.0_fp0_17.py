import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()

# Read the first two bytes to get the uncompressed size
uncompressed_size = int.from_bytes(data[:2], byteorder='little')

# Decompress the data
uncompressed_data = decompressor.decompress(data[2:])

# Check that we got the expected size
assert len(uncompressed_data) == uncompressed_size

# Check that the data is the same as the original
assert uncompressed_data == original_data
 
# Test LZMAFile
with lzma.open(filename, mode='rb') as f:
    assert f.read() == original_data
 
# Test LZMAFile with a custom filter chain
with lzma.open(filename, mode='rb', filters=[
        {"id": lzma.FILTER_LZMA2, "preset": 3 | lzma.PRESET_EXTREME}]) as f:
    assert f.read() == original_data
 
# Test LZMAFile with a
