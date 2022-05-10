import lzma
# Test LZMADecompressor's input property

dec = lzma.LZMADecompressor()
dec.input
with pytest.raises(AttributeError):
    dec.input = b"abc"

# Test LZMAInput too

dec = lzma.LZMADecompressor()

dec.input
with pytest.raises(AttributeError):
    dec.input = b"abc"

# Test LZMADecompressor's eof property
#
# Note that only LZMADecompressor.eof is tested here;
# LZMAOutput.eof and LZMAInput.eof have the same code.

dec = lzma.LZMADecompressor()
dec.eof
with pytest.raises(AttributeError):
    dec.eof = True

# Test LZMAInput too

dec = lzma.LZMADecompressor()
dec.eof
with pytest.raises(AttributeError):
    dec.eof = True
