import lzma
# Test LZMADecompressor.__init__
with pytest.raises(ValueError, match='Invalid format'):
    lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
with pytest.raises(ValueError, match='Invalid filters'):
    lzma.LZMADecompressor(filters=[])
with pytest.raises(ValueError, match='Invalid filters'):
    lzma.LZMADecompressor(filters=[{}])
with pytest.raises(ValueError, match='Invalid filters'):
    lzma.LZMADecompressor(filters=[{'id': lzma.FILTER_LZMA2}])
with pytest.raises(ValueError, match='Invalid filters'):
    lzma.LZMADecompressor(filters=[{'id': lzma.FILTER_DELTA}])
with pytest.raises(ValueError, match='Invalid filters'):
    lzma.LZMADecompressor(filters=[{'id
