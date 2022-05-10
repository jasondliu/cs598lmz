import bz2
# Test BZ2Decompressor.flush() method.
decompressor = bz2.BZ2Decompressor()
decompressor.flush()
# Test BZ2Compressor.flush() method.
compressor = bz2.BZ2Compressor()
compressor.flush()
def fix_encoding():
    # Tests for http://bugs.python.org/issue1170
    b = b'\xe9'
    try:
        codecs.lookup('utf-8').name
    except LookupError:
        # We can't test anything
        return
    encoding = 'utf-8'
    # Make sure the byte string is valid in the encoding.
    decoded = b.decode(encoding)
    # Encode it again.
    encoded = decoded.encode(encoding)
    # This will work, because the byte string is still valid.
    decoded.encode(encoding)
    # Decode it without a redirecting to the correct encoding.
    codecs.charmap_decode(b, 'strict', None, None)
    # Encode it again
