from lzma import LZMADecompressor
LZMADecompressor().decompress(s)

# 压缩数据
s = b'witch which has which witches wrist watch'
comp = LZMACompressor()
comp.compress(s)
comp.flush()

# 压缩文件
with open('lorem.txt', 'rb') as input:
    with lzma.open('lorem.xz', 'wt') as output:
        output.write(input.read())

# 解压文件
with lzma.open('lorem.xz') as f:
    text = f.read()

# 压缩文件
with open('lorem.txt', 'rb') as input:
    with lzma.open('lorem.xz', 'wt') as output:
        for line in input:
            output.write(line)
