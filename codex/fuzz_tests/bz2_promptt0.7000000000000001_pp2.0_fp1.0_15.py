import bz2
# Test BZ2Decompressor with the given file object.  Specify
# 'buffer_size' as the size of the read buffer and 'small_buffer' as
# the size of the decompression object's read buffer.  If
# 'expected_bz2_decompress_error' is not None, we expect that the
# BZ2Decompressor object will raise an exception when we feed it
# 'input_data' and that the exception object will match
# 'expected_bz2_decompress_error'.  Otherwise, we expect that the
# BZ2Decompressor object will return 'expected_output'.
def _test_bz2_decompressor(input_data, buffer_size, small_buffer,
expected_output, expected_bz2_decompress_error=None):
    input_file = BytesIO(input_data)
    decompressor = bz2.BZ2Decompressor()
    output = []
    while True:
        input_chunk = input_file.read(buffer_size)
        if not input_chunk:
            break
        if expected_b
