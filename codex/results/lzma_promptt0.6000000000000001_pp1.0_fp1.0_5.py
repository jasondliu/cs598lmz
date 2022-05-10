import lzma
# Test LZMADecompressor.decompress()

# The magic header of .xz files.
xz_header = b'\xfd7zXZ\x00'

def test_decompress_returns_unused_data(use_list_input):
    decompressor = lzma.LZMADecompressor()

    if use_list_input:
        input = [xz_header + lzma.compress(b'a') + b'b']
    else:
        input = xz_header + lzma.compress(b'a') + b'b'

    if use_list_input:
        unused_data = decompressor.decompress(input)
    else:
        unused_data = decompressor.decompress(input, 1)

    return unused_data

def test_decompress_handles_short_input(use_list_input):
    decompressor = lzma.LZMADecompressor()

    if use_list_input:
        input = [xz_header, lzma.compress(
