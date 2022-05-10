import bz2
# Test BZ2Decompressor using name attribute

decomp = bz2.BZ2Decompressor()
decomp.decompress(b('BZh91AY&SY'))
# Test BZ2Decompressor using decompress()

decomp = bz2.BZ2Decompressor()
decomp.decompress(b('BZh91AY&SY'))
decomp.flush()
# Test BZ2Decompressor context manager

with bz2.BZ2Decompressor() as decomp:
    decomp.decompress(b('BZh91AY&SY'))
# Test BZ2Decompressor.__del__

decomp = bz2.BZ2Decompressor()
decomp.decompress(b('BZh91AY&SY'))
del decomp
# This should raise an exception
# Test BZ2Decompressor without a source

decomp = bz2.BZ2Decompressor()
decomp.decompress(None)
# This should raise an exception
# Test BZ2Decompressor with a short source

