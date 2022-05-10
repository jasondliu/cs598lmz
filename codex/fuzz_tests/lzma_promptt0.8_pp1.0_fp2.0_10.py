import lzma
# Test LZMADecompressor.

text = 'Spam' * 1000000
compressed = lzma.compress(text)

decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(compressed)

assert data == text
# Test LZMADecompressor sequential use.

decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(compressed[:16])
assert data == ''
data = decompressor.decompress(compressed[16:])
assert data == text
# Test LZMADecompressor unsupported errors.

decompressor = lzma.LZMADecompressor()

with pytest.raises(ValueError) as excinfo:
    decompressor.decompress(compressed[:16], max_length=1)
assert excinfo.value.args == ('cannot specify max_length with LZMA',)

with pytest.raises(ValueError) as excinfo:
    decompressor.decompress(compressed, max_length
