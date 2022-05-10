import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

compressor.compress(b"foo")
compressor.compress(b"bar")

compressor.flush()

