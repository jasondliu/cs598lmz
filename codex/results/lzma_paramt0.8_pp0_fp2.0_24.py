from lzma import LZMADecompressor
LZMADecompressor.decompress
#<built-in method decompress of lzma.LZMADecompressor object at 0x7fad0edb9790>

#可以设置可选参数max_length来限制压缩区块的大小
compressor.compress(b'Binary data')
#b'\x00\x00\x00\x07\x00\x00\x00\x00\x13\x07Bin'
compressor.compress(b' more data')
#b' more data'
compressor.flush()
#b'\x00\x00\x00\x00'

decompressor.decompress(b'\x00\x00\x00\x07\x00\x00\x00\x00\x13\x07Bin')
#b'Binary data'
decompressor.decompress(b' more data')
#b' more data'

#如
