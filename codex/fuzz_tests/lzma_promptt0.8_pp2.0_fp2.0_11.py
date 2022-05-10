import lzma
# Test LZMADecompressor

# The following 3 invariants always hold:
#     0 <= next_in <= total_in <= len(input_buffer)
#     0 <= next_out <= total_out <= len(output_buffer)
#     0 <= unused_data <= len(unconsumed_tail) <= len(input_buffer)

# The compressed input is input_buffer[next_in:total_in]
# The decompresssed output is output_buffer[next_out:total_out]
# The unconsumed input is input_buffer[total_in:total_in+unused_data]
# The unconsumed output is output_buffer[total_out:]

def decompress(input_data, expected_size,
               input_buffer_size=io.DEFAULT_BUFFER_SIZE,
               output_buffer_size=io.DEFAULT_BUFFER_SIZE):

    # sanity check
    assert lzma.decompress(b'') == b''

    d = lzma.LZMADecompressor()
    input_buffer = bytearray(input_buffer_size)
