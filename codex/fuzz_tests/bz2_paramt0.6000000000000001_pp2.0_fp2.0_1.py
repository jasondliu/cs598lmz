from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 压缩：
# 压缩内容是一个字节序列，可以是任意长度的。
# 压缩后的内容也是字节序列，但是长度要小于压缩前的。
# 压缩算法的工作过程是不可逆的。也就是说，压缩算法是不可逆的，无法通过解压缩的结果来确定压缩前的内容。
# 压缩算法的设计目标之一是尽可能减少空间
