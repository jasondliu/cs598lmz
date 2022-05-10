import bz2
# Test BZ2Decompressor
decom = bz2.BZ2Decompressor()
decom.decompress(bz2.compress(b'hello world!'))

# Test decompress file
