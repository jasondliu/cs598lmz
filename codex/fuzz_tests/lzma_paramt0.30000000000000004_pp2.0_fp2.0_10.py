from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 压缩数据
compressor = LZMACompressor()
compressor.compress(b"some data")
compressor.flush()

# 压缩文件
with open('/path/to/input', 'rb') as input, open('/path/to/output', 'wb') as output:
    compressor = LZMACompressor()
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(compressor.compress(chunk))
    output.write(compressor.flush())

# 解压文件
with open('/path/to/input', 'rb') as input, open('/path/to/output', 'wb') as output:
    decompressor = LZMADecompressor()
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# 压
