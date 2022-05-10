import lzma
# Test LZMADecompressor improperly, just to exercise the catch_break
# in LZMADecompressor.__init__
d = lzma.LZMADecompressor()
try:
    d.decompress(b'ham')
except RuntimeError as e:
    assert str(e).startswith('invalid input')
else:
    assert False

# Test LZMADecompressor.decompress() improperly
try:
    lzma.decompress(b'ham')
except RuntimeError as e:
    assert str(e).startswith('cannot determine the uncompressed size')
else:
    assert False


import lzma
assert isinstance(lzma.open(BytesIO(dumps(b'ham')), mode='rb',
                           format=lzma.FORMAT_ALONE), lzma.LZMAFile)
assert isinstance(lzma.open(BytesIO(dumps(b'ham')), mode='rb',
                           format=lzma.FORMAT_XZ), lzma.LZMAFile)

