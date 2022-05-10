import lzma
# Test LZMADecompressor.decompress()

# Test the decompressor with a simple file that has been compressed with
# LZMA.compress()

# The file is the first few lines of the Python license.

with open("LICENSE.txt", "rb") as f:
    license_text = f.read()

compressed = lzma.compress(license_text, format=lzma.FORMAT_ALONE)

decompressor = lzma.LZMADecompressor()

decompressed = decompressor.decompress(compressed)

assert license_text == decompressed

# The decompressor can be used as a context manager.

with lzma.LZMADecompressor() as decompressor:
    decompressed = decompressor.decompress(compressed)

assert license_text == decompressed


# Test that decompress() raises an exception when the input is truncated.

with pytest.raises(lzma.LZMAError):
    decompressor.decompress(compressed[:-10])

# Test that
