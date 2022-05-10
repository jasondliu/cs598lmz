import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b"Y*=RE\x05\x00LXJW\x01\x100\x00\x14")

import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14 \x00\x00\x00\x01\x01')

import lz4.frame
# Test LZ4Decompressor
decompressor = lz4.frame.LZ4Decompressor()
decompressor.decompress(b'\xf2\x48\xcd\xc9\xc9\x07\x00\x00')


# Test GzipDecompressor (uses decompress)
dec
