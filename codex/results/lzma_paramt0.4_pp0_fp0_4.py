from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 可以通过调用decompress()方法来多次解压数据
decompressor = LZMADecompressor()

while True:
    chunk = file.read(chunk_size)
    if not chunk:
        break
    data = decompressor.decompress(chunk)
    if data:
        print(data)
    else:
        break

# 如果数据块是经过压缩的，可以使用decompressobj()方法创建一个解压对象，
# 然后使用该对象的decompress()方法来解压数据。
# 如果解压后的数据不完整，
