from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'witch which has which witches wrist watch'

# 使用文件
import lzma, binascii
with lzma.open('lzma_compressed.xz', 'rb') as input, \
     open('lzma_decompressed.bin', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

# 解压缩比较大的文件
import lzma, binascii
with lzma.open('lzma_compressed.xz', 'rb') as input, \
     open('lzma_decompressed.bin', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    while True:
        block = input
