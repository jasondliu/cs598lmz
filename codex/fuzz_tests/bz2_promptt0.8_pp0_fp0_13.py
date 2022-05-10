import bz2
# Test BZ2Decompressor()
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b"BZh9\xccH\xcd\xc9\xc9W\x08\x00\x00\x00\x10\x00\x00\x00l$\x19\x01\x00\x0f]\xeb\xff\xff>\x9f\x00\x00\x00")
decompressor.flush()
# b'*** False\n*** False\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n*** True\n***
