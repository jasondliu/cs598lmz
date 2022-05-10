from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 使用默认的模式，压缩文件
with lzma.open('foo.xz', 'wt') as f:
    f.write('这是一个测试文件')

# 使用指定的模式，解压文件
with lzma.open('foo.xz', 'rt', encoding='utf-8') as f:
    text = f.read()

# 压缩文件
with lzma.open('foo.xz', 'wt', preset=9) as f:
    f.write('这是一个测试文
