import lzma
# Test LZMADecompressor.eof()
compressor = lzma.LZMACompressor()
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressor.compress(data)
compressor.flush()

decompressor = lzma.LZMADecompressor()
print(decompressor.eof)  # False
decompressor.decompress(b'')
print(decompressor.eof)  # False
