import bz2
# Test BZ2Decompressor with multiple streams and data after the first EOF
data = b'12345678' * 1024
compobj = bz2.BZ2Compressor()
compressed1 = compobj.compress(data)
compressed1 += compobj.flush()
compobj = bz2.BZ2Compressor()
compressed2 = compobj.compress(data)
compressed2 += compobj.flush()
compobj = bz2.BZ2Compressor()
compressed3 = compobj.compress(data)
compressed3 += compobj.flush()
compressed = compressed1 + compressed2 + compressed3
test_data = b"".join(
    [compressed, compressed[:10], compressed[10:20], b'hello ', b'and ',
     b'goodbye', b'hello again'])
dcompobj = bz2.BZ2Decompressor()
decompressed = dcompobj.decompress(test_data)
decompressed += dcompobj.unused_data
