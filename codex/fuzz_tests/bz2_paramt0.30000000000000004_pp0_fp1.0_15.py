from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 如果只有少量的数据需要被压缩，则可以使用压缩后的数据作为单独的字符串存储起来。
# 为了将数据压缩成一个字符串，可以使用 io.BytesIO() 来包装一个字节流，然后像文件一样操作它。
import bz2

uncompressed_data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


