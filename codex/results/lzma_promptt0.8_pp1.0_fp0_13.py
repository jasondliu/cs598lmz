import lzma
# Test LZMADecompressor with a raw stream.
d = lzma.LZMADecompressor()
decompressed = d.decompress(b'\x5d\x00\x00\xff'*1024)
len(decompressed)

decompressed == b'X'*10240
# The LZMADecompressor class automatically decompresses
# the data as it comes in. This is very useful when working
# with files.
with lzma.open('data/lzma_compressed') as original:
    with lzma.open(original, format=lzma.FORMAT_ALONE) as uncompressed:
        uncompressed.read() == b'This is the original text. '*100
# Repeated reads from the same LZMADecompressor object will
# keep returning the same data.
with lzma.open('data/lzma_compressed') as original:
    with lzma.open(original, format=lzma.FORMAT_ALONE) as uncompressed:
        uncompressed.read() == uncompressed.read()


