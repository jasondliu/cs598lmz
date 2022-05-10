from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用文件对象来包装内存中的压缩数据流
from io import BytesIO
compressed = BytesIO(data)
decompressor = LZMADecompressor()

while True:
    chunk = compressed.read(10)
    if not chunk:
        break
    print(decompressor.decompress(chunk))
