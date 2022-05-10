from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# 创建一个压缩的文件
with lzma.open('file.xz', 'wb') as dest:
    dest.write(b'hello world')

# 使用lzma对象创建一个文件解压缩器
decompressor = LZMADecompressor()
with lzma.open('file.xz') as compressed:
    with open('uncompressed-file', 'wb') as decompressed:
        while True:
            chunk = compressed.read(1024)
            if not chunk:
                break
            decompressed.write(decompressor.decompress(chunk))
