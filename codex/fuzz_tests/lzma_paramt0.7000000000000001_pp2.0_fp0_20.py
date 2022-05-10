from lzma import LZMADecompressor
LZMADecompressor().decompress()

# 默认情况下，如果输入数据是比块大小小的，那么就会引发错误。 你可以更改块大小来覆盖它：
# 如果你想要自己控制处理的块的大小，可以使用参数unconsumed_data
d = LZMADecompressor(format=FORMAT_RAW, memlimit=MEMLIMIT_DATA, filters=[{'id': FILTER_LZMA2, 'preset': 3}])
d.decompress(b'\xFF' * 10, max_length=5)
d.unconsumed_tail
d.decompress(b'X' * 5)
d.dec
