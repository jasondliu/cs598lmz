import lzma
# Test LZMADecompressor
# Test if high level API is able to handle arbitrary-size input and output
def test_compressed_data_chunks(input_size=1 << 18, *, *, use_check=True):
    # Use the max possible match length is 18, i.e. 262144 - 1 bytes
    assert get_dict_size(18) == input_size
    # Generate a bytestring that can be compressed by LZMA algorithm
    # Use ``randint`` instead of ``getrandbits`` to avoid generating leading
    # zeros which will cause failures of ``hexlify``
    data = input_data * (input_size // len(input_data) + 1)
    cdata_list = []
    f = io.BytesIO()
    with lzma.LZMACompressor(format=lzma.FORMAT_RAW, check=lzma.CHECK_NONE) \
            as compressor:
        compressor.compress(data[:input_size - 5])
        while True:
            compressed = compressor.compress(data[:randint(0, 100)])
