from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output:
# b'hello'

# 注意，LZMADecompressor 对象可以多次调用 decompress() 方法来处理数据块流。
# 例如：

import lzma

compressor = lzma.LZMACompressor()
chunk1 = compressor.compress(b'This is the first chunk of data. ')
chunk2 = compressor.compress(b'And this is the second one. ')
chunk3 = compressor.compress(b'And finally the third one.')
chunk4 = compressor.flush()

# Write the chunks to a file.

