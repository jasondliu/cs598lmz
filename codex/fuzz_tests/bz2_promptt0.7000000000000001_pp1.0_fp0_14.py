import bz2
# Test BZ2Decompressor.decompress()

def make_data():
    return b'X' * 4 + b'Y' * 5 + b'Z' * 6

def make_compressed_data():
    compressor = bz2.BZ2Compressor()
    compressor.compress(b'X' * 4)
    compressor.flush(bz2.BZ_FLUSH)
    compressor.compress(b'Y' * 5)
    compressor.flush(bz2.BZ_FLUSH)
    compressor.compress(b'Z' * 6)
    compressor.flush(bz2.BZ_FINISH)
    return compressor.compress(b'X' * 4) + compressor.flush() + \
           compressor.compress(b'Y' * 5) + compressor.flush() + \
           compressor.compress(b'Z' * 6) + compressor.flush()

def check_decompress(input, expected_output):
    try:
        decompressor = bz2.BZ2Decompressor()
        output = decompressor.decompress
