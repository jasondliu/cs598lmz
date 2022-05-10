import bz2
# Test BZ2Decompressor and compressobj

for compressor in (bz2.BZ2Compressor, bz2.BZ2Decompressor):
    obj = compressor()
    obj.compress(b"foo")
    obj.flush()
    obj.close()
    try:
        obj.compress(b"foo")
    except ValueError:
        pass
    else:
        print("%s.close() didn't raise ValueError" % obj.__class__.__name__)

# Test BZ2File and BZ2Compressor

for (input, mode, output) in ((b"foo", 'wb', b'BZh9\x88\x13\x00\x00\x00\x00\x00\x002\x8e\x02\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00'),
                              (b"foo", 'rb', b'foo'),
                              (io.BytesIO(b"foo"), 'wb', b'BZh9\x88\
