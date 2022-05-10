import lzma
# Test LZMADecompressor

data = b"X" * 100 + lzma.compress(b"test") + b"Y" * 100

decomp = lzma.LZMADecompressor()

decomp.decompress(data)

decomp.decompress(b"end")

decomp.flush()

decomp.unused_data

decomp.unconsumed_tail
len(decomp.unconsumed_tail)

decomp.decompress(b"bad")

decomp.decompress(b"good")

decomp.flush()

decomp.unused_data

decomp.unconsumed_tail
len(decomp.unconsumed_tail)

decomp.decompress(b"")

decomp.flush()

decomp.unused_data

decomp.unconsumed_tail
len(decomp.unconsumed_tail)

decomp.decompress(b"bad")

decomp.decompress(b"good")

decomp.flush()

