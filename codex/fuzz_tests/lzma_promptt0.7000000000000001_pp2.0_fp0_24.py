import lzma
# Test LZMADecompressor.flush()
data = lzma.compress(b"test") + b"\1"
dec = lzma.LZMADecompressor()
dec.decompress(data)
dec.flush()

print('dec.eof =', dec.eof)
# Test LZMADecompressor.__del__()
dec = lzma.LZMADecompressor()
dec.decompress(data)
dec.__del__()

print('eof=%d, unconsumed_tail=%d' % (dec.eof, len(dec.un
