from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# 添加消息头
LZMADecompressor.decompress(data, format=FORMAT_RAW)[1:]

# 添加消息头
LZMADecompressor.decompress(data, format=FORMAT_XZ)[1:]

# 添加消息头
LZMADecompressor.decompress(data, format=FORMAT_ALONE)[1:]

# 添加消息头
LZMADecompressor.decompress(data, format=FORMAT_RAW)[1:]

# 添加消息头
LZMADecompressor.decompress(data, format=FORMAT_XZ)[1:]

# 添加消息头
LZMADecompressor.decompress(data, format=FORMAT_ALONE)[1:]

#
