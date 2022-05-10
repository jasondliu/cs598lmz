from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# 压缩到文件
with open('xz_compressed.xz', 'wb') as dest:
    with lzma.open('file.txt', 'rt',
                   encoding='utf-8',
                   errors='ignore') as src:
        dest.write(src.read().encode('utf-8'))

# 也可以在一个文件上进行压缩和解压
with lzma.open('file.txt.xz', 'rt') as file:
    print(file.read())

# 压缩率控制
with lzma.open('file-3.txt', 'wt') as file:
    file.write(text)
with open('file-3.txt', 'rb') as input:
    data = input.read()
with lzma.open('file-3.txt.xz', 'wt', preset=9 | lzma
