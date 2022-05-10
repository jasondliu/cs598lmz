import bz2
bz2.decompress(bz2.compress(b'binary\x00string'))

# 可以看到，bz2.compress()的效率比zlib.compress()高很多，因为它压缩更严格，
# 压缩比更小。

# 尽管如此，就压缩率而言，bz2.compress()的效果还是比不上zlib.compress()的。
# 通常，bz2.compress()的效率更高，所以，如果你能接受更小的压缩比，就可以使用它。

# 小
