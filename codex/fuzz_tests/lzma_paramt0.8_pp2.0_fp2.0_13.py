from lzma import LZMADecompressor
LZMADecompressor().decompress(c)

# 使用bz2
import bz2

with bz2.open('file.bz2', 'wt', encoding='utf-8') as f:
    f.write(c)
with bz2.open('file.bz2', 'rt', encoding='utf-8') as f:
    print(f.read())
