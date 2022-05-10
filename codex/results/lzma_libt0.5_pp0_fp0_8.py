import lzma
lzma.LZMAFile(open('/usr/share/dict/words.xz'))

# 它支持更高级的压缩和解压缩选项，但是大多数情况下，lzma.compress() 和 lzma.decompress() 就足够了
raw = b"Hello World"
len(raw)
compressed = lzma.compress(raw)
len(compressed)
lzma.decompress(compressed)

# 如果你想使用基于文件的压缩工具，但是又不想使用系统命令，可以使用 zlib 模块。
# 它提供了一个类似
