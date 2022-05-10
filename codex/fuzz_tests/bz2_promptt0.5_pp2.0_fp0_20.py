import bz2
# Test BZ2Decompressor class

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(bz2.compress(b"testing"))

decompressor.decompress(bz2.compress(b"testing"))

decompressor.decompress(bz2.compress(b"testing"))

decompressor.flush()

decompressor.decompress(bz2.compress(b"testing"))

decompressor.decompress(bz2.compress(b"testing"))

decompressor.decompress(bz2.compress(b"testing"))

decompressor.decompress(bz2.compress(b"testing"))

decompressor.flush()

decompressor.decompress(bz2.compress(b"testing"))

decompressor.decompress(bz2.compress(b"testing"))

decompressor.flush()
