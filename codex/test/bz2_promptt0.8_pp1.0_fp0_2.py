import bz2
# Test BZ2Decompressor.
def test_bz2_decompressor():
    compressor = bz2.BZ2Compressor()
    # Compress an empty string. The compression block is not flushed yet.
    empty_string = b''
    compressed_empty_string = compressor.compress(empty_string)
    assert compressed_empty_string == b''

    # Flush an empty byte from the compression block. This can be done
    # multiple times.
    compressed_empty_string = compressor.flush()
    assert compressed_empty_string == b'BZh91AY&SY\x90\x00\x00\x00\x19\x80\x01\x00\x00\x00\x01\x00\x02@\x00\x82\x00\x19\x12\x0bU\xe6\x82\xb2\x1d\x04\x01\x00\x00\x00'

    # Non-empty string compression
    compressor = bz2.BZ2Compressor()
    string = b'Python is a programming language'
